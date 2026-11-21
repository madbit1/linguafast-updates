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
      if (n < 34) return;
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
        34: "Aligned translation cards, expandable history and provider controls, and a redesigned secure APK downloader (device verification ongoing)."
      };
      description.textContent = summaries[n] ||
        "A newer signed LinguaFast APK is available. Check the official release notes for the full list of changes.";
      link.href = "https://github.com/madbit1/linguafast-updates/releases/tag/android-v" + n;
    })
    .catch(() => { /* Keep published v34 fallback without interrupting the page. */ });
})();