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
      if (n < 23) return;
      const expected = "LinguaFast_v" + n + "_Update.apk";
      if (!release.assets.some(a => a && a.name === expected && a.size > 0)) return;
      const label = n === 23 ? "v1.23.0" : "Android build " + n;
      version.textContent = label;
      status.textContent = "Latest public GitHub release · build " + n;
      description.textContent = n === 23
        ? "Per-provider encrypted API key profiles, local Android Keystore storage and easier switching between AI services."
        : "A newer signed GitHub release is available. Open its official release notes to see what changed.";
      link.href = "https://github.com/madbit1/linguafast-updates/releases/tag/android-v" + n;
    })
    .catch(() => { /* Keep verified v23 fallback without interrupting the page. */ });
})();