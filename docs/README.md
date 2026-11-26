# LinguaFast — official product website

**Canonical public site:** https://madbit1.github.io/linguafast/  
**Source:** this public repository, `madbit1/linguafast`, branch `main`. The Android application source and signing keys are maintained separately and privately.

**Latest independently confirmed published Android APK at this update:** v1.41.0 / build 41, release [android-v41](https://github.com/madbit1/linguafast-updates/releases/tag/android-v41), SHA-256 `ca91090c0bf19bc71982860151c0b319adcb162c1a1772d7b7f46a0e93b415ff`. The owner's Samsung Termux publisher uploaded and downloaded back the matching signed asset and verified the public update feed on 25 November 2026. On-phone installation and microphone layout verification are still unconfirmed. The live release panel uses the GitHub latest-release API and can update after a later signed release is published.

## Pages and maintenance

- `index.html`: feature overview, clearly labelled historical v36 illustration, current v41 functionality, three-step Quick Setup guide and live GitHub release card
- `support.html`: user help for the Quick Setup, Android system-language labels, microphone placement, AI keys, dictation, updates and saved local data
- `privacy.html`: privacy notice aligned with v41 published flows and the locally handled new setup (no extra AI calls simply to choose a language)
- `site.js`: read-only latest signed APK lookup with independently confirmed v41 fallback, v37–v42 descriptions and conditional setup availability; no analytics or keys
- `images/linguafast-v36-translate.svg`: privacy-safe v36 main-screen illustration; all text is example data
- `style.css`, `favicon.svg`, `robots.txt`, `sitemap.xml`: styling and metadata

The public repository `madbit1/linguafast-updates` contains a **legacy duplicate website** in its `docs/` directory. Keep it synchronized or direct readers to this canonical site; do not publish contradictory release/privacy notices. The update repository is binary-only for releases; never upload private Android app source, secrets, signing material or personal data.

## Accuracy and safety

Website phone and chat examples are **illustrations, not screenshots** or proof of translation correctness. The secure in-app updater was confirmed on the user's Samsung through v36; v41 GitHub publication and checksum have been independently confirmed, but successful v41 phone installation has not been established here. The user still approves Android installation. Play Protect and Samsung Auto Blocker must not be bypassed. GitHub releases are not Google Play approval.

Outstanding before Play distribution: genuine device screenshots, verified private developer and privacy contact, legal review, platform policy and data-safety review, and an approved Play build/AAB. Pricing for optional AI depends on the user's selected provider; speech accuracy depends on installed Android speech services.

## Current in-progress app follow-up

The private LinguaFast source branch `fix/v42-complete-setup-20261126` adds a guided first-run Quick Setup, keeping the old settings and encrypted AI vault, plus a shorter Guest C Auto-detect dropdown label. Source tests cover layout, stored-data retention and the 12 supported UI locales. **No signed v42 APK is claimed on this public website unless the GitHub release feed confirms one.** This public repository contains only product information and public site files; the Android source and signing material remain private.
