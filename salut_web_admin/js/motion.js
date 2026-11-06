/**
 * Gerak terarah halaman admin (Motion versi vanilla dari CDN, versi dipatok di tag <script>).
 * Hanya empat hal: konten masuk halaman, angka statistik naik dari 0 ke nilai dari API,
 * baris tabel muncul bertahap, dan dialog modal muncul halus saat dibuka.
 * Dilewati seluruhnya jika Motion gagal dimuat atau pengguna memilih prefers-reduced-motion.
 */
(function () {
    'use strict';
    var M = window.Motion;
    if (!M || typeof M.animate !== 'function') return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    // 1. Konten masuk halaman
    var content = document.querySelector('.content');
    if (content) {
        M.animate(content, { opacity: [0, 1], transform: ['translateY(6px)', 'translateY(0px)'] }, { duration: 0.2, ease: 'easeOut' })
            .then(function () { content.style.removeProperty('transform'); });
    }

    // 2. Angka statistik (elemen bertanda data-count): animasikan sekali, saat halaman mengisi angkanya
    document.querySelectorAll('[data-count]').forEach(function (el) {
        var observer = new MutationObserver(function () {
            var text = el.textContent.trim();
            var target = Number(text);
            if (text === '' || !isFinite(target)) return; // masih "—" atau belum terisi
            observer.disconnect();
            M.animate(0, target, {
                duration: 0.6,
                ease: 'easeOut',
                onUpdate: function (v) { el.textContent = Math.round(v); },
                onComplete: function () { el.textContent = text; }
            });
        });
        observer.observe(el, { childList: true, characterData: true, subtree: true });
    });

    // 3. Baris tabel muncul bertahap (12 baris pertama) saat halaman merender tabel baru
    function animateRows(root) {
        var rows = Array.prototype.slice.call(root.querySelectorAll('tbody tr'), 0, 12);
        if (!rows.length) return;
        M.animate(rows, { opacity: [0, 1], transform: ['translateY(4px)', 'translateY(0px)'] },
            { duration: 0.18, delay: M.stagger(0.02), ease: 'easeOut' })
            .then(function () { rows.forEach(function (r) { r.style.removeProperty('transform'); }); });
    }
    new MutationObserver(function (mutations) {
        mutations.forEach(function (m) {
            m.addedNodes.forEach(function (n) {
                if (n.nodeType === 1 && (n.matches('.table-wrap') || n.querySelector('.table-wrap tbody'))) animateRows(n);
            });
        });
    }).observe(document.querySelector('.content') || document.body, { childList: true, subtree: true });

    // 4. Modal: isi dialog muncul halus saat dibuka (penutupan langsung, karena halaman memakai display:none)
    document.querySelectorAll('.modal-overlay').forEach(function (overlay) {
        var modal = overlay.querySelector('.modal');
        if (!modal) return;
        new MutationObserver(function () {
            if (!overlay.classList.contains('show')) return;
            M.animate(modal, { opacity: [0, 1], transform: ['translateY(8px)', 'translateY(0px)'] }, { duration: 0.18, ease: 'easeOut' })
                .then(function () { modal.style.removeProperty('transform'); });
        }).observe(overlay, { attributes: true, attributeFilter: ['class'] });
    });
})();
