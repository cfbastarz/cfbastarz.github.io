// Apply the saved palette before styles load to avoid a flash of light content.
(function () {
    let choice = 'system';
    try { choice = localStorage.getItem('cfbasz-theme') || 'system'; } catch (_) {}
    if (!['system', 'light', 'dark'].includes(choice)) choice = 'system';
    const dark = choice === 'dark' || (choice === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches);
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    document.documentElement.dataset.themePreference = choice;
}());
