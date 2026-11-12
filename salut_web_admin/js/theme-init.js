/* Terapkan tema tersimpan (salut_theme) sebelum halaman digambar, supaya tidak berkedip. Dimuat di <head>. */
(function () {
    var theme = 'dark';
    try { theme = localStorage.getItem('salut_theme') || 'dark'; } catch (e) { /* penyimpanan tidak tersedia */ }
    document.documentElement.setAttribute('data-theme', theme);
})();
