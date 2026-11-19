# LinguaFast — security and safe installation

**Last reviewed:** 19 November 2026. This document covers the public signed-APK channel, not a Google Play store listing.

## Current distribution and known issue

A previous installation attempt on Samsung showed Google Play Protect **“Harmful app blocked”** and Samsung Auto Blocker **“Unknown app blocked.”** The exact Google classification reason and remediation are **not established**, so do not assume a false positive or say the app is security-cleared. No user should be instructed to disable Play Protect/Auto Blocker or choose an override to install a flagged APK.

The last owner-verified **public** release is [android-v19](https://github.com/madbit1/linguafast-updates/releases/tag/android-v19); build 20 was locally signed and verified on 19 November 2026 but is **not a confirmed public release**. Always consult [GitHub Releases](https://github.com/madbit1/linguafast-updates/releases/latest) for the actual visible distribution status.

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
