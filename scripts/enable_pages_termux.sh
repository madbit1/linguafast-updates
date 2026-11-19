#!/usr/bin/env bash
# LinguaFast: one-time enablement of free GitHub Pages in the EXISTING
# public releases repository. Uses Termux's already authenticated GitHub CLI.
# Does not change APKs, secrets, release versions or the private source.
set -euo pipefail
REPO="madbit1/linguafast-updates"
URL="https://madbit1.github.io/linguafast-updates/"
echo "Setting up LinguaFast website via existing GitHub account..."
command -v gh >/dev/null 2>&1 || { echo "GitHub CLI (gh) missing. Open https://github.com/$REPO/settings/pages"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "GitHub CLI not authenticated. Use the existing GitHub account or configure Pages in Settings."; exit 1; }
if gh api "repos/$REPO/pages" --jq '.html_url' >/dev/null 2>&1; then
  BRANCH="$(gh api "repos/$REPO/pages" --jq '.source.branch // ""')"
  FOLDER="$(gh api "repos/$REPO/pages" --jq '.source.path // ""')"
  if [[ "$BRANCH" != main || "$FOLDER" != /docs ]]; then
    echo "GitHub Pages already uses $BRANCH:$FOLDER; existing setup NOT modified."
    echo "Go to https://github.com/$REPO/settings/pages"
    echo "Choose Source: Deploy from a branch | main | /docs | Save."
    exit 1
  fi
  echo "GitHub Pages already configured for main:/docs."
else
  echo "Creating GitHub Pages site from main:/docs..."
  if ! gh api -X POST "repos/$REPO/pages" \
     -f 'source[branch]=main' -f 'source[path]=/docs' \
     --jq '.html_url'; then
    echo "Automatic enablement failed. No release files changed."
    echo "Open https://github.com/$REPO/settings/pages"
    echo "Choose Source: Deploy from a branch | main | /docs | Save."
    exit 1
  fi
fi
echo
echo "CONFIGURED GITHUB PAGES: $URL"
echo "Privacy: "$URL"privacy.html"
echo "Support: "$URL"support.html"
echo "The website must complete publishing before the link responds; check repository Settings → Pages for status."
