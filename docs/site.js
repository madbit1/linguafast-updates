/* Latest release metadata only. No analytics, cookies or user credentials. */
(() => {
  "use strict";
  const version = document.getElementById("release-version");
  const status = document.getElementById("release-state");
  const description = document.getElementById("release-copy");
  const link = document.getElementById("release-link");
  if (!version || !status || !description || !link || !window.fetch) return;
  const endpoint = "https://api.github.com/repos/madbit1/linguafast-updates/releases/latest";
  fetch(endpoint, { headers: { Accept: "application/vnd.github+json" } })
    .then(response => { if (!response.ok) throw new Error("Release metadata unavailable"); return response.json(); })
    .then(release => {
      const found = /^android-v([1-9][0-9]*)$/.exec(String(release && release.tag_name || ""));
      if (!found || !Array.isArray(release.assets)) return;
      const n = Number(found[1]);
      if (n < 41) return;
      const expected = "LinguaFast_v" + n + "_Update.apk";
      if (!release.assets.some(a => a && a.name === expected && a.size > 0)) return;
      version.textContent = "v1." + n + ".0";
      status.textContent = "Latest public GitHub release · build " + n;
      const summaries = {
        23: "Independent encrypted AI key profiles for multiple providers.",
        24: "Updated Android app distribution and AI-provider configuration.",
        25: "Separate AI-provider rows and a main-screen AI-channel selector.",
        26: "Better wrapping of saved original and translated text.",
        27: "Full bilingual History and Saved cards with one Copy both control.",
        28: "Update progress pop-up, Android download percentage, checksum validation and clear installation handoff.",
        29: "Longer voice recording pauses, improved final speech recognition, and cursor-based dictation for Translate and Conversation drafts.",
        30: "Improved update recovery when Samsung Download Manager stalls.",
        31: "Verified APKs stored in a dedicated LinguaFast Downloads folder.",
        32: "Cleaner Translate and Conversation switching and larger live chat area.",
        33: "One-tap AI Polish and Undo for Translate and typed Conversation drafts, plus a clearer chat boundary.",
        34: "Aligned translation cards, expandable history and provider controls, and a redesigned secure APK downloader.",
        35: "In-app updater resumes after installation-source permission; borderless Translate icons and accessible History/Saved.",
        36: "Thumb-sized borderless icons in one row, readable and tappable bilingual History/Saved cards; updater confirmed working on Samsung.",
        37: "Longer AI translations, opt-in provider failover and WhatsApp Smart Split, with cross-language tone safeguards.",
        38: "Animated AI Polish status stays inside the small toolbar icon.",
        39: "Clearer FROM/TO language boxes, compact icons and automatic source-language preview.",
        40: "Conversation language choices and 12-language phone-localized main interface labels.",
        41: "Speaker A, B and Guest C microphones are kept above the scrolling conversation on smaller screens.",
        42: "New-user Quick Setup for text and conversation languages with optional secure AI-key setup; Guest C Auto-detect label is shorter."
      };
      description.textContent = summaries[n] ||
        "A newer signed LinguaFast APK is available. Check the official release notes for the full list of changes.";
      link.href = "https://github.com/madbit1/linguafast-updates/releases/tag/android-v" + n;
      const setupNote = document.getElementById("quick-setup-availability");
      if (setupNote && n >= 42) setupNote.textContent =
        "The signed v42 update includes Quick Setup on fresh Android installations, and it stays accessible from Help. It will not reset existing saved language choices, history or encrypted AI settings.";
    })
    .catch(() => { /* Keep independently verified v41 fallback without interrupting the page. */ });
})();