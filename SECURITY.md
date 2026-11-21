# LinguaFast — security and safe installation

## Current state — 21 November 2026 (v34)

**Published:** [android-v34](https://github.com/madbit1/linguafast-updates/releases/tag/android-v34), APK `LinguaFast_v34_Update.apk`, owner-confirmed SHA-256 `198565a6dae17750b07ab31374a97cbb1f47514e054486692ba7e5ae3bb7c2e2` from local signing/validation and GitHub download-back verification.

In v34 Android 10+ the app has a new direct HTTPS update download intended to avoid stuck Download Manager jobs. Downloads are kept pending until the APK matches the published SHA-256 twice; the installer still independently checks the signing identity and requires approval. SDK <29 retains Download Manager. **The v34 in-app downloader has not yet been verified end-to-end on the affected Samsung device; do not describe the issue as conclusively fixed.**

A prior Google Play Protect **“Harmful app blocked”** warning remains unresolved. Integrity checks are not malware certification. **Never disable or override Play Protect or Samsung Auto Blocker warnings.** Existing compatible upgrades should preserve data; do not uninstall to force an update. Do not publish signing keys, source code, personal conversation history or tokens to this repository.

Official website: https://madbit1.github.io/linguafast/ — [privacy](https://madbit1.github.io/linguafast/privacy.html) · [support](https://madbit1.github.io/linguafast/support.html).

---

## Historical security review notes (older releases; superseded current-status statements below)

## Current release (19 November 2026)

The owner published [signed LinguaFast android-v21](https://github.com/madbit1/linguafast-updates/releases/tag/android-v21) with APK/checksum assets. The publisher downloaded the public APK back and verified SHA-256 `3e05073969d9f41218aa72ea0d34fdff54d382c6e9d4d0f9a53ceb14f9e34440`. The current v21 code also verifies a downloaded update against the matching GitHub `.sha256` file before Android installer handoff; **real on-device behavior has not been validated**. The prior Play Protect **“Harmful app blocked”** report is unresolved, not necessarily reproduced on v21. Signature and digest matching are integrity checks, **not proof that the APK is safe**. Never override Play Protect/Auto Blocker to install a flagged app.


**Last reviewed:** 19 November 2026. This document covers the public signed-APK channel, not a Google Play store listing.

## 19 November 2026 — current release and review status

**Public v20 is available:** https://github.com/madbit1/linguafast-updates/releases/tag/android-v20, APK SHA-256 `e9d3ecc85d4903e12e5f7ad21de36c94e8ab683ae565aa4d6abf308ba63e0318`, with owner-confirmed upload and downloaded-back checksum match. This is a **public GitHub sideload distribution**, not an independently cleared app-store release or malware-free certification.

The private developer source now has an **unpublished v21** improvement: before its own Android installer handoff, the app checks downloaded APK bytes against the corresponding GitHub `.sha256` sidecar and blocks the handoff on error. **This fix is not included in the publicly released v20 APK.** Native compilation, Samsung behavior and Play Protect status for v21 remain untested.

For the prior **“Harmful app blocked”** warning, the affected binary/version is not conclusively identified by the historical screenshot. Follow [Google's developer guidance](https://developers.google.com/android/play-protect/warning-dev-guidance) and, after proper review if classification appears erroneous, the [official appeal form](https://support.google.com/googleplay/android-developer/contact/protectappeals). The form requests the APK's VirusTotal SHA-256 and supporting details. No appeal or Google clearance is claimed. **Do not bypass Play Protect or Samsung security checks.**

## Current distribution and known issue

A previous installation attempt on Samsung showed Google Play Protect **“Harmful app blocked”** and Samsung Auto Blocker **“Unknown app blocked.”** The exact Google classification reason and remediation are **not established**, so do not assume a false positive or say the app is security-cleared. No user should be instructed to disable Play Protect/Auto Blocker or choose an override to install a flagged APK.

The latest owner-confirmed **public release is [android-v20](https://github.com/madbit1/linguafast-updates/releases/tag/android-v20)**, signed APK `LinguaFast_v20_Update.apk`, SHA-256 `e9d3ecc85d4903e12e5f7ad21de36c94e8ab683ae565aa4d6abf308ba63e0318`. Owner's Termux output verifies GitHub upload, download-back SHA-256 match and published status. **The classification of the previous harmful-app warning, a separate unauthenticated `releases/latest` check and successful on-device v20 installation remain unverified.** No statement here certifies the APK as safe or recommends overriding security protections.

## Release integrity checks

The trusted Android package ID is `com.linguafast.translatox`. The existing signing certificate SHA-256 is `a41fd999b6f63545ff07c11be4f02166e32a0b693b128b8de3417b690f8fc869`.

A standard approved release uses a strictly increasing Android build code, original signing certificate, APK signature verification, matching package/version, a published SHA-256 checksum, a download-back checksum comparison and a live public release-feed check. These checks verify **identity and integrity**, not absence of malware or legality.

This repository is **binary-only**. Do not upload developer keystores, signing material, authentication tokens, private source, personal chat transcripts or private user data. The Android installer requires user approval for updates. Never promise silent installs or instruct users to uninstall a working version to force an upgrade.

## Open release-gate work

Before expanding to general public distribution:
1. Investigate the exact Play Protect warning classification, relevant APK/dependencies/manifest and Android speech/installer behaviour. If appropriate, request Google's official review/appeal: https://developers.google.com/android/play-protect/warning-dev-guidance
2. Document a defensible release approval and test the real Samsung update with security protections enabled.
3. Publish a verified developer privacy contact, confirm data protection requirements and keep the app's in-app Privacy and data notice consistent with [the public privacy policy](PRIVACY_POLICY.md).
4. Improve the downloaded APK's in-app digest verification before handing it to the package installer; the GitHub publisher's own SHA-256 verification is not a substitute for a client-side check.
5. Keep Google Play distribution separate: it requires a policy-compliant AAB and Play-managed updates, not the existing GitHub self-installer.

## Reporting a security problem

Do **not** include secrets, personal conversations or signing keys in public GitHub issues. A verified private security-contact route has not yet been published. Until one exists, this project does **not** claim an established confidential vulnerability reporting program. Developers should establish an approved contact and update this document before promoting LinguaFast as production-ready.
