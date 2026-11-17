#!/usr/bin/env python3
"""Reusable signed Android APK publisher. No version numbers are hard-coded.

Requires config/app.json (stable app identity), release-input/manifest.json,
release-input/ready.json and a validated signed APK (path or base64 parts).
Publishes to the binary-only GitHub repo, never the private source repo.
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
def fail(reason):
    raise SystemExit("RELEASE BLOCKED: " + reason)
def read_json(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))
def tool(name):
    found = shutil.which(name)
    if found:
        return found
    home = os.environ.get("ANDROID_HOME") or os.environ.get("ANDROID_SDK_ROOT") or ""
    matches = sorted((Path(home) / "build-tools").glob("*/" + name)) if home else []
    if matches:
        return str(matches[-1])
    fail(f"Android SDK Build Tools ({name}) not installed; release NOT published")
def run(args, **kwargs):
    return subprocess.run(args, text=True, check=True, capture_output=True, **kwargs).stdout.strip()
def require_hex(value):
    return isinstance(value, str) and re.fullmatch(r"[a-fA-F0-9]{64}", value) is not None

def publish(apk_override=None, validate_only=False):
    config = read_json("config/app.json")
    manifest = read_json("release-input/manifest.json")
    ready = read_json("release-input/ready.json")
    expected_keys = ("app_name", "asset_prefix", "application_id", "signing_certificate_sha256", "release_repo")
    if any(not isinstance(config.get(k), str) or not config[k] for k in expected_keys):
        fail("incomplete stable app config")
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]*", config["asset_prefix"]):
        fail("invalid APK asset prefix")
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.]*(?:\.[A-Za-z][A-Za-z0-9_]*)+", config["application_id"]):
        fail("invalid Android package ID")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", config["release_repo"]):
        fail("invalid release repository")
    if not require_hex(config["signing_certificate_sha256"]):
        fail("invalid release signing-certificate fingerprint")
    repo = config["release_repo"]
    if os.environ.get("GITHUB_REPOSITORY", repo) != repo:
        fail("running in a repository other than the approved public release repository")

    code = manifest.get("build_code")
    name = manifest.get("version_name")
    digest = manifest.get("sha256")
    if type(code) is not int or code < 1 or code >= 2100000000:
        fail("release build_code must be a positive Android integer")
    if not isinstance(name, str) or not re.fullmatch(r"[0-9]+(?:\.[0-9]+){1,3}", name):
        fail("release version_name must be numeric, e.g. 1.13.0")
    if not require_hex(digest):
        fail("release SHA-256 missing or invalid")
    if ready.get("build_code") != code or ready.get("sha256") != digest:
        fail("ready marker and signed APK manifest do not match")
    if manifest.get("schema_version") != 1 or ready.get("schema_version") != 1:
        fail("unsupported release manifest schema")

    filename = f'{config["asset_prefix"]}_v{code}_Update.apk'
    tag = f"android-v{code}"
    if apk_override:
        payload = Path(apk_override).read_bytes()
    else:
        parts = manifest.get("parts")
        if not isinstance(parts, list) or not parts or len(parts) > 1024:
            fail("release payload has no ordered base64 parts")
        b64 = []
        for p in parts:
            if not isinstance(p, str) or not re.fullmatch(r"release-input/payload/part[0-9]{4}\.b64", p):
                fail("invalid release payload part filename")
            b64.append("".join((ROOT / p).read_text(encoding="ascii").split()))
        try:
            payload = base64.b64decode("".join(b64), validate=True)
        except Exception:
            fail("signed APK payload could not be decoded")
    actual = hashlib.sha256(payload).hexdigest()
    if actual.lower() != digest.lower():
        fail(f"SHA-256 mismatch; expected {digest}, got {actual}")
    with tempfile.TemporaryDirectory() as tmp:
        apk = Path(tmp) / filename
        apk.write_bytes(payload)
        try:
            with zipfile.ZipFile(apk) as z:
                if z.testzip() is not None:
                    fail("APK ZIP CRC failed")
                if not {"AndroidManifest.xml", "classes.dex", "assets/index.html"} <= set(z.namelist()):
                    fail("missing required Android APK files")
                ui = z.read("assets/index.html").decode("utf-8")
                if f"INSTALLED_BUILD_CODE={code};" not in ui:
                    fail("About version/build in APK disagrees with manifest")
                url = f"https://api.github.com/repos/{repo}/releases/latest"
                if url not in ui:
                    fail("embedded update feed does not match publishing destination")
        except zipfile.BadZipFile:
            fail("not an Android APK archive")

        try:
            aapt = run([tool("aapt"), "dump", "badging", str(apk)])
            package_match = re.search(
                r"^package: name='([^']+)' versionCode='([0-9]+)' versionName='([^']+)'",
                aapt, re.MULTILINE)
            if not package_match:
                fail("unable to read package/version from Android binary manifest")
            app_id, installed_code, installed_name = package_match.groups()
            if app_id != config["application_id"] or int(installed_code) != code or installed_name != name:
                fail("Android package ID/version mismatch")
            signature = run([tool("apksigner"), "verify", "--verbose", "--print-certs", str(apk)])
            cert = re.search(r"Signer #1 certificate SHA-256 digest:\s*([0-9a-fA-F]+)", signature)
            if not cert or cert.group(1).lower() != config["signing_certificate_sha256"].lower():
                fail("APK signing certificate does not match installed-app identity")
            if not re.search(r"Verified using v[23] scheme .*:\s*true", signature):
                fail("no verified modern Android APK signature")
        except subprocess.CalledProcessError as e:
            fail("Android APK signature/manifest verification failed: " + e.stderr[-350:])
        print(f"PASS {tag}: package={app_id}, version={name}, SHA-256={actual}, certificate matches")
        if validate_only:
            return

        if not shutil.which("gh"):
            fail("authenticated GitHub CLI (gh) is required")
        if not os.environ.get("GH_TOKEN"):
            fail("GH_TOKEN is required for release publishing; never embed it in the APK")
        visibility = run(["gh", "repo", "view", repo, "--json", "visibility", "--jq", ".visibility"])
        if visibility.upper() != "PUBLIC":
            fail("target release repository is not public")
        previous = json.loads(run(["gh", "release", "list", "-R", repo, "--limit", "100", "--json", "tagName"]))
        codes = [int(m.group(1)) for item in previous
                 if (m := re.fullmatch(r"android-v([0-9]+)", item["tagName"]))]
        if codes and code <= max(codes):
            fail("release build_code is not newer than the existing release; do not overwrite or downgrade")
        note = str(manifest.get("release_notes") or f"{config['app_name']} {name} signed Android update.")
        if len(note) > 20000:
            fail("release notes too long")
        checksum = Path(tmp) / (filename + ".sha256")
        checksum.write_text(f"{actual}  {filename}\n", encoding="ascii")
        notes = Path(tmp) / "release-notes.txt"
        notes.write_text(note + f"\n\nPackage: {app_id}\nBuild: {code}\nSHA-256: {actual}\n"
                         "Install through Android Package Installer; retain existing app data.\n",
                         encoding="utf-8")
        run(["gh", "release", "create", tag, str(apk), str(checksum), "-R", repo,
             "--title", f"{config['app_name']} {name} (build {code})",
             "--notes-file", str(notes), "--latest"])
        # Verify the specific release exists and contains the named signed APK.
        released = json.loads(run(["gh", "release", "view", tag, "-R", repo, "--json", "tagName,assets"]))
        if released.get("tagName") != tag or filename not in [x["name"] for x in released["assets"]]:
            fail("release created but signed APK asset not confirmed")
        print(f"RELEASE CONFIRMED: https://github.com/{repo}/releases/tag/{tag}")
        try:
            request = urllib.request.Request(
                f"https://api.github.com/repos/{repo}/releases/latest",
                headers={"User-Agent": "LinguaFast-release-verifier", "Accept": "application/vnd.github+json"})
            with urllib.request.urlopen(request, timeout=20) as response:
                latest = json.load(response)
            if latest.get("tag_name") == tag:
                print("PUBLIC UPDATE FEED CONFIRMED: latest release is visible without credentials")
            else:
                print("WARNING: GitHub public latest-feed propagation pending; manual test still required")
        except Exception as e:
            print("WARNING: Public latest-feed check pending:", type(e).__name__)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apk", help="use already-signed APK from local or CI file instead of release-input/payload parts")
    parser.add_argument("--validate-only", action="store_true", help="test without publishing")
    args = parser.parse_args()
    publish(args.apk, args.validate_only)
