# LinguaFast — public signed Android releases

## Current published release — 21 November 2026

**Latest owner-confirmed release:** [LinguaFast v1.36.0 / build 36](https://github.com/madbit1/linguafast-updates/releases/tag/android-v36). The signed `LinguaFast_v36_Update.apk` was built and verified on the owner's Samsung in Termux, published on GitHub and downloaded back with SHA-256 `4458dc6c58d5dbb72d0bb6090d1c0c9ec88bedc9dabff1ab955c3d761615a35f`. **The owner then confirmed a successful in-app update to v36 and supplied screenshots from the installed device.** This is confirmation of one tested Samsung update, not a guarantee for every Android device or network.

**What's new:** v35 restored large borderless Translate shortcuts and a working permission handoff; v36 retains one horizontal row of thumb-sized icons, makes History and Saved entries readable at full height and tappable, and preserves the successful in-app updater. The user's screenshots confirm the layout improvements and live translation, but do not independently confirm every saved-record action.

**Official public product website:** https://madbit1.github.io/linguafast/ (source `madbit1/linguafast`). This repository retains a synchronized **legacy website copy** in `docs/`, including a privacy-safe SVG illustration representing the v36 interface. Examples are illustrations, not the owner's private conversations or genuine screenshots.

### Distribution and safety
Only approved signed APKs and their checksums belong in release assets; never upload private app source, signing keys or user records. Keep package ID `com.linguafast.translatox` and the existing signing certificate unchanged. Do not uninstall the app or clear data for an update, and do not bypass any harmful-app Play Protect or Samsung security warning. GitHub sideload distribution is not Google Play Store approval.

---

## Historical release preparation notes (superseded by v36 status above)



## LinguaFast website and Google Play preparation

The official LinguaFast information website is prepared in the public [`docs/`](docs/) folder: product homepage, responsive CSS and illustrations, current GitHub release metadata, [privacy policy](docs/privacy.html) and [support/help](docs/support.html). It uses LinguaFast's real Android feature set and v23 release; any on-page phone or conversation examples are identified as **illustrations, not authentic screenshots**. Real Samsung screenshots still need to be captured for the Play listing.

**Free website address (once GitHub Pages is activated):** https://madbit1.github.io/linguafast-updates/ . Hosting is on GitHub Pages, not Vercel. The deployment workflow is [`deploy-website.yml`](.github/workflows/deploy-website.yml), deploying `docs/` on website changes; the owner must activate Pages once using repository administration. A first automated run failed with `Resource not accessible by integration` while attempting to create the Pages site; **do not claim the URL is live until a successful Pages deployment is verified**.

From an existing authenticated GitHub CLI (e.g., the same Termux installation used to publish APKs), an owner may activate Pages for GitHub Actions and dispatch the website workflow:

```sh
gh api -X POST repos/madbit1/linguafast-updates/pages -f build_type=workflow --jq .html_url
gh workflow run deploy-website.yml -R madbit1/linguafast-updates
```

If the first command reports an already-existing Pages site, use `gh api -X PUT repos/madbit1/linguafast-updates/pages -f build_type=workflow` instead. The GitHub Pages site can also be enabled at https://github.com/madbit1/linguafast-updates/settings/pages by selecting **GitHub Actions**.

**Remaining for Google Play, independently of this website:** app-bundle publishing instead of only APK; target API 36+ (current source targets 35); removing the sideload self-install permission and self-update flow from the Play variant; accurate Data Safety declarations; a verified, private developer support/privacy contact; genuine screenshots; Play developer account and possible closed-test/identity requirements; investigation of the earlier Play Protect warning. Do not bypass device security.


## Official LinguaFast website — free GitHub Pages

The public product website source is in [`docs/`](docs/), separate from the private app source and from signed APK release assets. Its planned HTTPS address is **https://madbit1.github.io/linguafast-updates/**, with a dedicated [privacy page](docs/privacy.html) and [support/data deletion page](docs/support.html). It shows the current v23 Android capabilities, explicitly labelled illustrative previews, and a read-only public GitHub release lookup.

**Site source has been committed and validated; Pages publishing must be switched on once.** From the already authenticated Termux `gh` CLI: `gh api -X POST repos/madbit1/linguafast-updates/pages -f 'source[branch]=main' -f 'source[path]=/docs'`. Alternatively use [repository Settings → Pages](https://github.com/madbit1/linguafast-updates/settings/pages), Source “Deploy from a branch”, Branch `main`, Folder `/docs`. The site should only be called live after verifying its HTTPS URL. No Vercel or another hosting account is used. Actual Android screenshots and a verified private support/contact address are still pending for Play Store review.



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
