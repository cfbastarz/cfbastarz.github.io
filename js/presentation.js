(function () {
    'use strict';
    const viewer = document.querySelector('.slide-viewer');
    if (!viewer) return;
    const slides = JSON.parse(viewer.dataset.slides);
    const image = viewer.querySelector('.slide-image');
    const select = viewer.querySelector('select');
    const status = viewer.querySelector('.slide-status');
    const previous = viewer.querySelector('[data-action="previous"]');
    const next = viewer.querySelector('[data-action="next"]');
    const fullscreen = viewer.querySelector('[data-action="fullscreen"]');
    let current = 1;
    function fromHash() {
        const match = /^#slide=(\d+)$/.exec(window.location.hash);
        return match ? Number(match[1]) : 1;
    }
    function show(number, updateLink) {
        current = Math.max(1, Math.min(slides.length, number));
        const slide = slides[current - 1];
        image.width = slide.width;
        image.height = slide.height;
        image.src = slide.url;
        image.alt = 'Slide ' + current + ' de ' + slides.length;
        select.value = String(current);
        previous.disabled = current === 1;
        next.disabled = current === slides.length;
        document.querySelector('[data-slide-number]').textContent = current;
        document.querySelector('[data-slide-text]').textContent = slide.text || 'Este slide não contém texto extraível. Consulte a imagem ou abra o PDF.';
        status.textContent = 'Slide ' + current + ' de ' + slides.length;
        if (updateLink) history.replaceState(null, '', '#slide=' + current);
        if (slides[current]) { const preload = new Image(); preload.src = slides[current].url; }
    }
    previous.addEventListener('click', function () { show(current - 1, true); });
    next.addEventListener('click', function () { show(current + 1, true); });
    select.addEventListener('change', function () { show(Number(select.value), true); });
    viewer.addEventListener('keydown', function (event) {
        if (event.target.tagName === 'SELECT' || event.altKey || event.ctrlKey || event.metaKey) return;
        const actions = {ArrowLeft: current - 1, ArrowRight: current + 1, Home: 1, End: slides.length};
        if (Object.prototype.hasOwnProperty.call(actions, event.key)) {
            event.preventDefault(); event.stopPropagation(); show(actions[event.key], true);
        }
    });
    window.addEventListener('hashchange', function () { show(fromHash(), false); });
    viewer.querySelector('[data-action="share"]').addEventListener('click', async function () {
        const link = new URL(window.location.href); link.hash = 'slide=' + current;
        try {
            await navigator.clipboard.writeText(link.href);
            status.textContent = 'Link do slide copiado.';
        } catch (_) { status.textContent = 'Copie este link: ' + link.href; }
    });
    if (!viewer.requestFullscreen || !document.fullscreenEnabled) fullscreen.hidden = true;
    fullscreen.addEventListener('click', async function () {
        try {
            if (document.fullscreenElement === viewer) await document.exitFullscreen();
            else await viewer.requestFullscreen();
        } catch (_) { status.textContent = 'Tela cheia indisponível. Você pode abrir o PDF pelo link abaixo.'; }
    });
    document.addEventListener('fullscreenchange', function () {
        fullscreen.textContent = document.fullscreenElement === viewer ? 'Sair da tela cheia' : 'Tela cheia';
    });
    image.addEventListener('error', function () { status.textContent = 'Não foi possível carregar o slide. Abra o PDF pelo link abaixo.'; });
    viewer.querySelector('.slide-toolbar').hidden = false;
    show(fromHash(), false);
}());
