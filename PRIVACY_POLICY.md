# LinguaFast — Privacy and data use

**Last updated:** 21 November 2026  
**Developer credit:** Stylish Future Technologies  
**Product:** LinguaFast Android application, package `com.linguafast.translatox`  
**Current public release:** v1.34.0 / build34

**Status:** This notice explains the features and data flows evident in the current application source. The developer has **not yet published a verified privacy contact/controller address or completed a documented legal/provider assessment**. Those items must be completed before describing the app as production-approved or broadly releasing a new version. This is not a claim of UK GDPR, EU GDPR or Google Play compliance.

## What information the app uses

LinguaFast works with the text you enter, speech-to-text transcripts, languages you select, translations, optional AI instructions, and settings. When you choose to save or keep records, these may include your own or other people's words; avoid putting confidential or sensitive information into public translation or AI services.

The app can use Android's microphone permission when you tap a voice-input control. The installed Android speech-recognition provider may process spoken audio locally or send it to a remote service; the app does **not** guarantee offline voice recognition or prevent the speech provider from processing audio under its own policy.

## Where the information goes

- **Local device:** translated/history records, up to 200 translation records, up to 200 conversation messages, up to 200 saved translations, up to 40 reusable source phrases, drafts, language choices, playback, voice and theme preferences, and non-secret AI settings are stored in private WebView local storage when available. In Android v23, opted-in AI provider secrets are stored separately in app-private Android Keystore-backed encrypted storage. ML Kit **text language identification** is performed on-device.
- **Online translation:** when you translate, text and required language information are sent to the selected public translation service. The current instant path uses a Google translation endpoint, with MyMemory as fallback. Long text may be divided into several separate requests. Those services may process and retain information under their own terms.
- **Optional AI:** enabling AI translation or Polish sends the request text plus your API key for authorization to the service/provider you choose (for example Gemini, Groq, OpenRouter, OpenAI, DeepSeek or a custom compatible provider). Long AI messages are processed as multiple smaller provider requests where applicable; this may increase API usage or charges. AI providers may independently decline certain text; the app cannot guarantee uncensored responses. Their collection, billing, retention and cross-border processing arrangements vary.
- **Speech provider:** Android's installed recognition service may receive audio and return a transcript. Recognized text may then be sent to translation/AI providers as appropriate.
- **Updates:** LinguaFast checks public GitHub release metadata and, on user request, downloads a signed APK. On Android 10+ the v34 updater uses a direct HTTPS connection, stores downloaded bytes in a pending file and verifies the published SHA-256 twice before exposing an APK for the Android installer. Older Android versions retain Android Download Manager. This newly released update path is still awaiting real-device verification. Network operators and providers may see ordinary connection metadata such as IP addresses. The app's signing key and your personal API keys are not intended to be uploaded to GitHub.
- **Sharing and backups:** Copy, Android sharing, and manual JSON backup put information into the clipboard or apps you select. Clipboard backups are **not encrypted**; the built-in record backup excludes AI API keys. Treat the contents as personal data.

This notice does not assert that external service operators do not log or retain requests. To understand or request removal of provider-held records, consult the relevant provider's privacy policy and support channels.

## One-tap AI Polish and Undo (v33+)

When you tap Polish on a typed/dictated draft in Translate or the Conversation draft field, the current draft text is sent to the selected AI provider. On a successful response, the corrected text replaces the draft automatically. Undo restores the previous exact text locally and requires **no new AI provider request**. No continuous per-keystroke AI proofreading is used, and live conversation speech is not silently polished. Long messages may be split into separate provider calls. The original is retained if the AI request fails; later user edits invalidate the older Undo to avoid overwriting new text. Provider billing and data processing still apply to the Polish request.

## Your controls, retention and deletion

Translation history and conversations default to a **365-day** age limit, adjustable to **30 days, 90 days, 365 days, or keep until deleted**, with the record caps above. Missing timestamps from migrated records are assigned a migration-date anchor to avoid silently discarding them. Saved favourites and reusable phrases remain until deleted or affected by storage limits.

From **Privacy and data** in the app, you can copy a local JSON backup, restore/merge a backup, change retention, or **Clear local data**. History and individual conversation messages also have deletion controls. Clearing app storage or uninstalling may permanently remove your records; Android automatic backup is disabled. A compatible, originally signed in-place update is intended to preserve existing storage.

**Remember AI keys** is optional: in Android v23 and later, remembered keys are encrypted per provider using app-private SharedPreferences and Android Keystore AES-256-GCM. A v22 key is migrated only after a successful encrypted write; if migration fails, the app may retain the old local value rather than silently losing it. Different providers have independent key/model/URL profiles. Unchecking Remember and saving removes persistent provider keys; the selected key remains usable only within the current session. The browser edition uses opt-in unencrypted localStorage instead of Android Keystore. The app does not provide cross-device key recovery. Do not use untrusted devices for sensitive credentials.

Deleting content on your phone **does not erase copies already handled by external translation, AI, speech or sharing services**. Backups made outside the app must be managed separately.

## Security

The current Android manifest requests Internet, microphone, and package-install permission used for the optional user-approved GitHub update process. It disables Android automatic backup. Normal app updates must retain the package ID and signing identity. Security reviews are ongoing; no guarantee of risk-free software is made.

A previous attempted installation displayed Google Play Protect's **“Harmful app blocked”** warning. The cause has not been established. **Do not disable Android/Samsung security protections or override a harmful-app warning.** See [Security and release review](SECURITY.md).

## Privacy requests and contact

**A verified developer privacy/support contact has not yet been approved for publication.** The [LinguaFast support page](https://madbit1.github.io/linguafast/support.html) contains a non-private GitHub issue channel for ordinary support questions; never post private transcripts or API keys there. A private contact route must be supplied before Play submission. Until that contact is supplied and a rights/request-handling procedure is verified, users cannot rely on a published centralized controller request route. For device-only records, use the app's local privacy controls. For external provider data, contact those providers directly.

Before a general production release, the developer must publish its true contact identity/region and suitable privacy-request channel; document purposes, lawful bases where required, actual provider contracts and transfers, retention and deletion handling, rights-request response handling, and applicable child/consent safeguards. This notice will then be revised with verified facts rather than invented details.

## Changes to this notice

The public repository keeps this notice visible. Material changes to collection, providers, security or retention should be reviewed alongside new APK source and release notes. This privacy document can change independently of app-version numbers, but the in-app disclosure should be aligned before a general public rollout.
