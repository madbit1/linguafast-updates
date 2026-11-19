# LinguaFast website — public static files

This folder is the **only** source for the public LinguaFast landing site (separate from the private Android app source). It uses the real Android app's brand colour (`#0d9488`), documented v23 features, and verified v23 public release; private source, signing keys, user data and API keys are **never published here**.

## Live address and activation

Preferred free GitHub Pages URL (once enabled): **https://madbit1.github.io/linguafast-updates/**

The repository administrator can configure Pages to publish from **main /docs** using [Settings → Pages](https://github.com/madbit1/linguafast-updates/settings/pages), or run `bash scripts/enable_pages_termux.sh` from a local checkout of **this public repository** with an authenticated GitHub CLI. Note: the private Termux checkout `~/linguafast-src` is a *different* Git repository.

Web pages:
- `index.html`: product landing page, current features, illustrative interface panels and latest-release metadata
- `privacy.html`: current v23 Android privacy and data-deletion notice
- `support.html`: AI provider help, voice assistance, deletion process and Play submission status
- `site.js`: unauthenticated read-only GitHub release metadata lookup (fallback is owner-verified v23). No API secrets or analytics
- `favicon.svg`, `style.css`, `sitemap.xml`, `robots.txt`: shared styling/metadata

## Publishing and app-store review

Changes in `/docs` should be reviewed before publishing because this site contains legal/privacy claims. The current app's public privacy notice at `../PRIVACY_POLICY.md` also requires review and synchronisation when data flows change.

**Image authenticity:** Neither the public release repository nor the private source repository currently contains real Android screenshots, photographs, or store-banner files. The phone and conversation panels on the landing page are clearly labelled *illustrations*. Only replace them with genuinely captured and reviewed screenshots from the actual current LinguaFast Android version. Google Play submission requires authentic device screenshots.

**Still required before Play listing:** a verified non-public developer/support/privacy contact, policy review, real screenshots, Play App Bundle targeting Android API 36+, Play-distribution build without GitHub sideload self-update, and any applicable account testing/identity checks. Existing GitHub APK releases are not Play Store certification.

**Cost:** GitHub Pages is free for the public repository. GitHub documents a recommended 1 GB source size and soft 100 GB monthly site-bandwidth limit. Website availability is only confirmed after GitHub Pages is enabled and the final URL responds.
