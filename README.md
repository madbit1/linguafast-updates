# LinguaFast — public signed Android APK releases

**Developer credit:** Stylish Future Technologies. This is the **public, binary-only distribution repository** for LinguaFast. Application source remains in the separate **private** repository `madbit1/chat-translator`. Never upload source, signing keys, passwords, tokens, microphone recordings, local history or user data here.

## Releases and current status — 19 November 2026

- **Latest published:** [LinguaFast v1.23.0 / Android build23](https://github.com/madbit1/linguafast-updates/releases/tag/android-v23); [`LinguaFast_v23_Update.apk`](https://github.com/madbit1/linguafast-updates/releases/download/android-v23/LinguaFast_v23_Update.apk). **SHA-256:** `fa9b756c0c0379b551d8405e28daa897c133f8b2f927d6512969b33d31a59ac9`. The owner's Termux publisher verified the release APK's signature and SHA-256, uploaded APK/checksum assets, downloaded the APK back and confirmed its checksum, then explicitly reported **`PUBLISHED`** and **`PUBLIC UPDATE FEED VERIFIED`**.
- **Previous release:** [android-v22](https://github.com/madbit1/linguafast-updates/releases/tag/android-v22), SHA-256 `16ceed60b943f4bb83faa8dfffb97dcd1033e51da2fdf623063a52df37b37d12`. Earlier releases stay intact.
- **v23 features:** each AI provider retains its own locally saved key, model and API URL; Android saves the secrets in a Keystore-backed encrypted vault and migrates the selected v22 key when possible. Current presets include Gemini, Groq, OpenRouter, OpenAI, DeepSeek and Custom; future presets receive independent slots. AI-provider content policies still apply.
- **Public update metadata endpoint:** `https://api.github.com/repos/madbit1/linguafast-updates/releases/latest`; the owner-confirmed release script checked it and verified v23 and the expected APK asset. Actual Android v23 installation, saved-key migration, app-update behavior and provider response still need on-device validation.
- **Trusted package:** `com.linguafast.translatox`. Original signing certificate SHA-256: `a41fd999b6f63545ff07c11be4f02166e32a0b693b128b8de3417b690f8fc869`. Maintain certificate/package continuity.
- **Security caution:** a previous update attempt showed Google Play Protect **“Harmful app blocked”** and Samsung Auto Blocker warnings. The root cause has not been resolved or independently established for v23. **Do not bypass a harmful-app block.** Read [Security](SECURITY.md). Signed uploads and digest checks establish integrity, not a malware-safety verdict. GitHub sideload builds are not Google Play certifications.


## What LinguaFast does

Translate text and speak translations, including a three-speaker A/B/C conversation. The v19 release included phrases, playback controls and AI privacy choices; **v20** improved microphone pause handling, provider-dependent spoken-language Auto identification, A-to-Guest-C routing, conversation scrolling and individual message Delete. **v21** adds verified APK checksum checking before Android installer handoff, improved AI processing for long messages, faithful profanity/slang translation and proofreading, and a request for unmasked Android speech transcription when the device supports it. AI providers may still reject content under their rules.

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
