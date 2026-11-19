# LinguaFast — public signed Android APK releases

**Developer credit:** Stylish Future Technologies. This is the **public, binary-only distribution repository** for LinguaFast. Application source remains in the separate **private** repository `madbit1/chat-translator`. Never upload source, signing keys, passwords, tokens, microphone recordings, local history or user data here.

## Releases and current status — 19 November 2026

- **Published:** [LinguaFast v1.20.0 / Android build 20](https://github.com/madbit1/linguafast-updates/releases/tag/android-v20), asset [`LinguaFast_v20_Update.apk`](https://github.com/madbit1/linguafast-updates/releases/download/android-v20/LinguaFast_v20_Update.apk). **SHA-256:** `e9d3ecc85d4903e12e5f7ad21de36c94e8ab683ae565aa4d6abf308ba63e0318`. The owner's Termux publishing log confirmed both APK/checksum uploads, public release and downloaded-APK SHA-256 match. This is a **sideload release**, not Google Play approval.
- **Previous release:** [android-v19](https://github.com/madbit1/linguafast-updates/releases/tag/android-v19), checksum `2f89b5290dfcf12e7d6f8e39ae6083debe848466e8a0d0639c3dc4ecd6d8222b`. Existing public versions are retained as immutable baselines.
- **Public update metadata feed:** `https://api.github.com/repos/madbit1/linguafast-updates/releases/latest`. The publisher reported publication of v20; independent app/device recognition and in-place upgrade still require testing.
- **Trusted package:** `com.linguafast.translatox`. **Original signing certificate SHA-256:** `a41fd999b6f63545ff07c11be4f02166e32a0b693b128b8de3417b690f8fc869`. Preserve both for compatible in-place updates.
- **Security caution:** a previous attempted installation showed Google Play Protect **“Harmful app blocked”** and Samsung Auto Blocker warnings; the cause is unresolved. **Do not override device protections** to install a flagged binary. See [Security](SECURITY.md). Publication and signature verification are not malware clearance.


## What LinguaFast does

Translate text and speak translations, including a three-speaker A/B/C conversation. The v19 release included phrases, playback controls and AI privacy choices; the **published v20 build** improves microphone pause handling, provider-dependent spoken-language Auto identification, A-to-Guest-C routing, conversation scrolling and individual message Delete.

Speech recognition quality and automatic spoken language switching depend on installed Android language services. Short words may be misheard; a manually selected source language remains the reliable fallback.

## Privacy and data protection

Read the [public Privacy and data use policy](PRIVACY_POLICY.md) before entering private text or enabling voice/AI. Translation sends text to online providers. Android speech services **may** process audio remotely; optional AI providers receive selected text and your API key. History, saved phrases, drafts and settings normally remain in private local app storage; the app offers retention/deletion and manual JSON backup. The default history/conversation retention is 365 days, adjustable in-app. Backups copied to the clipboard are not encrypted. Local deletion does not erase external service copies.

**Production-readiness limitation:** a verified developer privacy/security contact, formal service-provider and rights-process assessment and Play Protect resolution remain outstanding. Do not describe the existing sideload channel as Google Play-approved or as having finished a formal privacy compliance review.

## Release publication contract

**A successful Gradle build is only a candidate.** Before announcing a new version, the complete sequence is: reviewed private source and tests → incremented Android build → original-key signed APK → certificate/package/version/hash verification → approved public release → signed APK + checksum + non-sensitive release notes uploaded to GitHub → download-back SHA-256 verification → public `releases/latest` verification → device update/retained-data test.

**Owner's normal publisher:** `bash android/tools/build_publish_termux.sh` in the existing private Termux checkout performs the build, signed validation, GitHub publication and public-feed verification as one process. `--build-only` is intentionally **not** a public release. An already built and verified APK can be published **without rebuilding** using `bash android/tools/publish_signed_apk_termux.sh` **once release/security approval is complete**. Never upload binary bytes directly to the private source repository. The original signing key stays on the owner's device.

Existing releases are immutable recovery baselines: always increment `versionCode`; never overwrite a published tag, rename the app package or rotate the signature casually. Public releases should include the descriptive source-maintained notes and matching `.sha256` file.

The historical `scripts/publish_apk.py` and `.github/workflows/publish-apk.yml` are preserved alternate/baseline infrastructure, **not** evidence that an APK built in Termux automatically uploads when `--build-only` was selected. The in-use Termux GitHub CLI publisher is the authoritative local signing/publication path.

## Installing and updating

When a newer compatible, security-cleared release is actually available, an existing user can open LinguaFast, tap **About → Check now → Update now**, and follow the Android Package Installer's approval. A routine in-place update should preserve local history/settings; uninstalling or clearing app data may destroy them. Users should not be asked to use Termux, sign APKs, enter developer passwords or browse a source repository.

If Android or Google blocks an installation as harmful, **stop and follow official guidance** rather than disabling protections. Samsung's current real-device update behavior and data preservation must be verified per release; no promise of silent installation is made.

## For maintainers

Keep developer/release artifacts in the private repo; only approved public signed APKs, SHA-256 checksums, release metadata and reviewed non-sensitive documentation go here. The public [Privacy Policy](PRIVACY_POLICY.md) and [Security Policy](SECURITY.md) must be updated when the actual app's data flows, protections or known risks change. See the private project's `AGENTS.md`, `RELEASE_SYNC_POLICY.md`, `PROJECT_STATUS.md` and `DATA_PROTECTION_AND_RELEASE_READINESS.md` for engineering checklists.
