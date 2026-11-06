/**
 * ChartTheme — pengaturan Chart.js bersama (dashboard, tracer study).
 * Warna dibaca dari token tema di css/app.css dan diperbarui saat tema gelap/terang diganti.
 * Dataset menyebut warnanya lewat paletteVars (nama variabel CSS), bukan nilai warna.
 * Dimuat setelah js/chart.umd.min.js dan sebelum skrip halaman.
 */
const ChartTheme = {
    baseOptions: { responsive: true, maintainAspectRatio: false },
    barScales: { x: { grid: { display: false } } },

    cssVar(name) {
        return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    },

    /** Warna status alumni (sama di semua grafik); status lain memakai abu-abu slate */
    statusVar(label) {
        const map = {
            'Bekerja': '--chart-1',
            'Kuliah / Melanjutkan Studi': '--chart-2',
            'Wirausaha': '--chart-3',
            'Mencari Kerja': '--chart-4'
        };
        return map[label] || '--chart-6';
    },

    paint(chart) {
        chart.data.datasets.forEach(ds => {
            if (ds.paletteVars) ds.backgroundColor = ds.paletteVars.map(v => this.cssVar(v));
            if (chart.config.type === 'doughnut') ds.borderColor = this.cssVar('--surface');
        });
        chart.update('none');
    },

    apply() {
        Chart.defaults.color = this.cssVar('--chart-tick');
        Chart.defaults.borderColor = this.cssVar('--chart-grid');
        Object.values(Chart.instances).forEach(c => this.paint(c));
    },

    init() {
        Chart.defaults.font.family = this.cssVar('--font-ui');
        Chart.defaults.font.size = 12;
        this.apply();
        window.onThemeChange = () => this.apply();
        if (document.fonts) document.fonts.ready.then(() => Object.values(Chart.instances).forEach(c => c.update('none')));
    },

    /** Buat (atau buat ulang) grafik pada canvas, warnai dari tema, dan beri ringkasan teks untuk pembaca layar */
    make(id, config, summary) {
        const canvas = document.getElementById(id);
        const previous = Chart.getChart(canvas);
        if (previous) previous.destroy();
        const chart = new Chart(canvas, config);
        this.paint(chart);
        if (summary) canvas.setAttribute('aria-label', summary);
        return chart;
    }
};
ChartTheme.init();
