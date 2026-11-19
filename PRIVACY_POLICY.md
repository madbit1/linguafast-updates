# LinguaFast — Privacy and data use

**Last updated:** 19 November 2026  
**Developer credit:** Stylish Future Technologies  
**Product:** LinguaFast Android application, package `com.linguafast.translatox`

**Status:** This notice explains the features and data flows evident in the current application source. The developer has **not yet published a verified privacy contact/controller address or completed a documented legal/provider assessment**. Those items must be completed before describing the app as production-approved or broadly releasing a new version. This is not a claim of UK GDPR, EU GDPR or Google Play compliance.

## What information the app uses

LinguaFast works with the text you enter, speech-to-text transcripts, languages you select, translations, optional AI instructions, and settings. When you choose to save or keep records, these may include your own or other people's words; avoid putting confidential or sensitive information into public translation or AI services.

The app can use Android's microphone permission when you tap a voice-input control. The installed Android speech-recognition provider may process spoken audio locally or send it to a remote service; the app does **not** guarantee offline voice recognition or prevent the speech provider from processing audio under its own policy.

## Where the information goes

- **Local device:** translated/history records, up to 200 translation records, up to 200 conversation messages, up to 200 saved translations, up to 40 reusable source phrases, drafts, language choices, playback, voice and theme preferences, and optional AI configuration are stored in private WebView local storage when available. ML Kit **text language identification** is performed on-device.
- **Online translation:** when you translate, text and required language information are sent to the selected public translation service. The current instant path uses a Google translation endpoint, with MyMemory as fallback. Those services may process and retain information under their own terms.
- **Optional AI:** enabling AI translation or Polish sends the request text plus your API key for authorization to the service/provider you choose (for example Gemini, Groq, OpenRouter, OpenAI, DeepSeek or a custom compatible provider). Their collection, billing, retention and cross-border processing arrangements vary.
- **Speech provider:** Android's installed recognition service may receive audio and return a transcript. Recognized text may then be sent to translation/AI providers as appropriate.
- **Updates:** LinguaFast checks public GitHub release metadata to discover newer signed APK versions, and, on user request, downloads an update from GitHub. Network operators and providers may see ordinary connection metadata such as IP addresses. The app's signing key and your personal API keys are not intended to be uploaded to GitHub.
- **Sharing and backups:** Copy, Android sharing, and manual JSON backup put information into the clipboard or apps you select. Clipboard backups are **not encrypted**; the built-in record backup excludes AI API keys. Treat the contents as personal data.

This notice does not assert that external service operators do not log or retain requests. To understand or request removal of provider-held records, consult the relevant provider's privacy policy and support channels.

## Your controls, retention and deletion

Translation history and conversations default to a **365-day** age limit, adjustable to **30 days, 90 days, 365 days, or keep until deleted**, with the record caps above. Missing timestamps from migrated records are assigned a migration-date anchor to avoid silently discarding them. Saved favourites and reusable phrases remain until deleted or affected by storage limits.

From **Privacy and data** in the app, you can copy a local JSON backup, restore/merge a backup, change retention, or **Clear local data**. History and individual conversation messages also have deletion controls. Clearing app storage or uninstalling may permanently remove your records; Android automatic backup is disabled. A compatible, originally signed in-place update is intended to preserve existing storage.

**Remember AI key** is optional: if selected, an API key can persist in local WebView storage; if unselected, the key is only available in the current app session. Local key storage is **not** Android Keystore encryption. Do not use an untrusted device for sensitive credentials.

Deleting content on your phone **does not erase copies already handled by external translation, AI, speech or sharing services**. Backups made outside the app must be managed separately.

## Security

The current Android manifest requests Internet, microphone, and package-install permission used for the optional user-approved GitHub update process. It disables Android automatic backup. Normal app updates must retain the package ID and signing identity. Security reviews are ongoing; no guarantee of risk-free software is made.

A previous attempted installation displayed Google Play Protect's **“Harmful app blocked”** warning. The cause has not been established. **Do not disable Android/Samsung security protections or override a harmful-app warning.** See [Security and release review](SECURITY.md).

## Privacy requests and contact

**A verified developer privacy/support contact has not yet been approved for publication.** Until that contact is supplied and a rights/request-handling procedure is verified, users cannot rely on a published centralized controller request route. For device-only records, use the app's local privacy controls. For external provider data, contact those providers directly.

Before a general production release, the developer must publish its true contact identity/region and suitable privacy-request channel; document purposes, lawful bases where required, actual provider contracts and transfers, retention and deletion handling, rights-request response handling, and applicable child/consent safeguards. This notice will then be revised with verified facts rather than invented details.

## Changes to this notice

The public repository keeps this notice visible. Material changes to collection, providers, security or retention should be reviewed alongside new APK source and release notes. This privacy document can change independently of app-version numbers, but the in-app disclosure should be aligned before a general public rollout.
