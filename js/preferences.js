(function () {
    'use strict';
    const theme = document.getElementById('site-theme');
    const media = window.matchMedia('(prefers-color-scheme: dark)');
    theme.value = document.documentElement.dataset.themePreference || 'system';
    function apply() {
        document.documentElement.dataset.theme = theme.value === 'dark' || (theme.value === 'system' && media.matches) ? 'dark' : 'light';
        document.documentElement.dataset.themePreference = theme.value;
    }
    theme.addEventListener('change', function () {
        try { localStorage.setItem('cfbasz-theme', theme.value); } catch (_) {}
        apply();
    });
    media.addEventListener('change', apply);
    document.querySelector('.site-preferences').hidden = false;
}());
