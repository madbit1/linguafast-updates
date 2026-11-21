# Legacy copy of LinguaFast website

This folder is a synchronized mirror of the canonical public product website at https://madbit1.github.io/linguafast/ (repository `madbit1/linguafast`). The repository `madbit1/linguafast-updates` serves signed APK assets, release metadata and security/privacy notices. For the most up-to-date product and support descriptions, use the canonical site.

# LinguaFast — official product website

**Canonical public site:** https://madbit1.github.io/linguafast/  
**Source:** this public repository, `madbit1/linguafast`, branch `main`. The Android application source and signing keys are maintained separately and privately.

**Latest documented published Android APK:** v1.34.0 / build 34, release [android-v34](https://github.com/madbit1/linguafast-updates/releases/tag/android-v34), SHA-256 `198565a6dae17750b07ab31374a97cbb1f47514e054486692ba7e5ae3bb7c2e2`. This SHA was confirmed by the owner's Termux local validation and GitHub download-back verification on 21 November 2026. The actual Samsung in-app v34 updater still requires a future-release end-to-end test.

## Pages and maintenance

- `index.html`: accessible feature overview, **illustrative** UI showing original above translated text, one-tap Polish/Undo, A/B/C conversation and release information
- `support.html`: user help for dictation, Polish, layout, update failures and local data
- `privacy.html`: privacy notice aligned with v34 flows (manual AI requests, direct APK download and local storage)
- `site.js`: read-only latest published release lookup, v34 static fallback, no analytics or keys
- `style.css`, `favicon.svg`, `robots.txt`, `sitemap.xml`: styling and metadata

The public repository `madbit1/linguafast-updates` contains a **legacy duplicate website** in its `docs/` directory. Keep it synchronized or direct readers to this canonical site; do not publish contradictory release/privacy notices. The update repository is binary-only for releases; never upload private Android app source, secrets, signing material or personal data.

## Accuracy and safety

Website phone and chat examples are **illustrations, not screenshots** or proof of translation correctness. The v34 direct-download implementation is a released code change, **not yet a confirmed on-device updater repair**. The user still approves Android installation. Play Protect and Samsung Auto Blocker must not be bypassed. GitHub releases are not Google Play approval.

Outstanding before Play distribution: genuine device screenshots, verified private developer and privacy contact, legal review, platform policy and data-safety review, and an approved Play build/AAB. Pricing for optional AI depends on the user's selected provider; speech accuracy depends on installed Android speech services.
