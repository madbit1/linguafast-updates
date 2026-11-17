# LinguaFast — public, signed APK update channel

This repository contains **only distribution metadata and signed Android APK files**. The application **source code remains private** in `madbit1/chat-translator`. Do not commit keystores, signing keys, secrets, API tokens, private source, app data or user histories here.

## Current live Android release

- **Latest published release:** [LinguaFast Android v13](https://github.com/madbit1/linguafast-updates/releases/latest)
- **In-app update feed:** `https://api.github.com/repos/madbit1/linguafast-updates/releases/latest`
- **Downloadable APK:** `LinguaFast_v13_Update.apk` — signed APK for **`com.linguafast.translatox`**, build **13**, version **1.13.0**.
- **APK SHA-256:** `5b6ca8589ed200a051c5a0982fde61bda4012f3ebca6b3e7f3d9ad179ad5d58f`
- **Signing certificate SHA-256:** `a41fd999b6f63545ff07c11be4f02166e32a0b693b128b8de3417b690f8fc869`
- **17 November 2026:** GitHub Actions run [44075803801](https://github.com/madbit1/linguafast-updates/actions/runs/44075803801) successfully verified signature, package version, APK digest, uploaded release asset, and anonymously accessible latest-release API.
- **Actual Android phone upgrade:** not yet user-tested. A live GitHub release does not silently install itself.

## Permanent rule — future builds are NOT hard-coded in the workflow

The [publisher](scripts/publish_apk.py) and [release workflow](.github/workflows/publish-apk.yml) are **version-independent**. **No version-number edits to scripts or workflow are needed for v14, v15 or later.** Each release is driven by:

1. **Stable app identity:** [`config/app.json`](config/app.json) defines package ID, certificate fingerprint, app name, and release repository. Those are **intentionally fixed security identifiers**, and should not change for routine version updates. A different Android app should have its own configuration and public binary-only release repo.
2. **New build metadata:** [`release-input/manifest.json`](release-input/manifest.json) states `build_code`, `version_name`, SHA-256, non-sensitive release notes, and ordered base64 payload part filenames.
3. **Signed package bytes:** the **already signed APK**, encoded as ordered base64 text chunks under `release-input/payload/` for this bootstrap transport. Every new build replaces the payload parts. No signing key is uploaded here.
4. **Publish signal:** update [`release-input/ready.json`](release-input/ready.json) **last**, with the matching `build_code` and checksum. That specific change triggers GitHub Actions. The workflow refuses a mismatch.
5. **Validation and publishing:** the workflow reassembles the APK, checks SHA-256, Android ZIP/manifest, embedded app version, v2/v3 signing identity, package ID, trusted update endpoint, and whether the build is newer than the last release. Only then does it publish `android-v<build_code>` and `LinguaFast_v<build_code>_Update.apk`.
6. **Verification:** the workflow checks its newly published Release and its public `releases/latest` feed. A user can then open **LinguaFast → About → Check Now** to see the new version and use Android's Package Installer to approve the update.

**Important:** For larger APKs, use a secure CI-built signed APK or locally generated payload chunks rather than attempting to commit a multi-megabyte base64 string in one GitHub file. The release script also supports `--apk /path/to/signed.apk` for an authorized build runner and `--validate-only` to test without publishing. Never distribute an installer before a signed asset is actually visible in the update feed.

## How app owners test the updater

When v12 is installed:

1. Open **About** or the version label.
2. Tap **Check Now**. It should show **v1.13.0 (build 13)** and **Get APK update**.
3. Tap **Get APK update**; Android should open the trusted release download in the browser.
4. Open the completed APK download from the Android notification or **Samsung My Files → Downloads** and approve **Package Installer → Update**.
5. Launch LinguaFast, confirm **v1.13.0 / build 13**, and verify that translations, history, and settings survived.

If Android does not launch the installer automatically, that's expected on unmanaged devices. If the update check fails or the download control does nothing, capture the exact screen/error for a targeted phone fix; don't replace the APK's package ID or signing key to work around it.

## Security policy

The public updater carries only signed binaries and public release metadata. The *private source* project is not made public. No secrets are included. Never overwrite an existing released build: publish the next strictly increasing Android `versionCode`. Do not remove the verified signing certificate or change the installed package ID. Source commits alone are not releases.
