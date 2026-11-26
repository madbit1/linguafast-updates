# LinguaFast — official product website

**Canonical public site:** https://madbit1.github.io/linguafast/  
**Source:** this public repository, `madbit1/linguafast`, branch `main`. The Android application source and signing keys are maintained separately and privately.

**Latest independently confirmed published Android APK at this update:** v1.42.0 / build 42, release [android-v42](https://github.com/madbit1/linguafast-updates/releases/tag/android-v42), APK SHA-256 `d3b1cd182cf7a1cbcb48026414f9e42253edb04cec812462d9d4284a4a2db05c`. GitHub `releases/latest` reports a non-draft, non-prerelease signed APK asset and matching digest, published on 26 November 2026. The complete APK bytes have not been independently compared against the current private source, and on-device installation/use remain to be confirmed.

## Pages and maintenance

- `index.html`: feature overview, clearly labelled historical v36 illustration, current v42 functionality, three-step Quick Setup guide and live GitHub release card
- `support.html`: user help for the Quick Setup, Android system-language labels, microphone placement, AI keys, dictation, updates and saved local data
- `privacy.html`: privacy notice aligned with v42 published flows and the locally handled new setup (no extra AI calls simply to choose a language)
- `site.js`: read-only latest signed APK lookup with independently confirmed v42 fallback, v37–v42 descriptions and conditional setup availability; no analytics or keys
- `images/linguafast-v36-translate.svg`: privacy-safe v36 main-screen illustration; all text is example data
- `style.css`, `favicon.svg`, `robots.txt`, `sitemap.xml`: styling and metadata

The public repository `madbit1/linguafast-updates` contains a **legacy duplicate website** in its `docs/` directory. Keep it synchronized or direct readers to this canonical site; do not publish contradictory release/privacy notices. The update repository is binary-only for releases; never upload private Android app source, secrets, signing material or personal data.

## Accuracy and safety

Website phone and chat examples are **illustrations, not screenshots** or proof of translation correctness. The secure in-app updater was confirmed on the user's Samsung through v36; v42 GitHub publication and APK digest have been independently confirmed, but successful v42 phone installation has not been established here. The user still approves Android installation. Play Protect and Samsung Auto Blocker must not be bypassed. GitHub releases are not Google Play approval.

Outstanding before Play distribution: genuine device screenshots, verified private developer and privacy contact, legal review, platform policy and data-safety review, and an approved Play build/AAB. Pricing for optional AI depends on the user's selected provider; speech accuracy depends on installed Android speech services.

## Current in-progress app follow-up

The published v42 release describes a guided first-run Quick Setup, keeping existing settings and encrypted AI keys, plus a shorter Guest C Auto-detect dropdown label. Source tests cover layout, stored-data retention and the 12 supported UI locales. GitHub confirms the signed v42 APK asset and checksum; live Samsung visual and microphone testing remain to be confirmed. This public repository contains only product information and public site files; the Android source and signing material remain private.
