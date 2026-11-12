/**
 * auth.js — Utilitas autentikasi & navigasi role-aware Web Admin SALUT
 * Mendukung role: admin (akses penuh) dan guru (akses terbatas)
 */
/**
 * Icons — satu set ikon SVG garis (stroke 1.75, grid 24). Sprite disuntik sekali di halaman ber-sidebar;
 * dipakai lewat Icons.svg('nama') atau <svg class="icon"><use href="#i-nama"/></svg>.
 */
const Icons = {
    paths: {
        'dashboard':      `<rect x="3" y="3" width="7" height="9" rx="1"/><rect x="14" y="3" width="7" height="5" rx="1"/><rect x="14" y="12" width="7" height="9" rx="1"/><rect x="3" y="16" width="7" height="5" rx="1"/>`,
        'users':          `<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c0-3.6 2.9-6 6.5-6s6.5 2.4 6.5 6"/><path d="M16 4.6a3.5 3.5 0 0 1 0 6.8"/><path d="M18 14.3c2.3.7 3.5 2.6 3.5 5.7"/>`,
        'clipboard-check':`<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9z"/><path d="m9 14 2 2 4-4"/>`,
        'badge-check':    `<circle cx="12" cy="9" r="6"/><path d="m9 9 2 2 3-3.5"/><path d="M8.5 14.5 7 21l5-3 5 3-1.5-6.5"/>`,
        'archive':        `<rect x="3" y="4" width="18" height="4" rx="1"/><path d="M5 8v11a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8"/><path d="M10 12h4"/>`,
        'flask':          `<path d="M9 3h6"/><path d="M10 3v6.2L4.8 18.2A1.5 1.5 0 0 0 6.1 20.5h11.8a1.5 1.5 0 0 0 1.3-2.3L14 9.2V3"/><path d="M7.5 15h9"/>`,
        'chart-bar':      `<path d="M4 20V10"/><path d="M10 20V4"/><path d="M16 20v-7"/><path d="M3 20h18"/>`,
        'calendar':       `<rect x="3.5" y="5" width="17" height="16" rx="2"/><path d="M8 3v4M16 3v4M3.5 10h17"/>`,
        'log-out':        `<path d="M9 4H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h3"/><path d="m16 8 4 4-4 4"/><path d="M20 12H9"/>`,
        'menu':           `<path d="M4 6h16M4 12h16M4 18h16"/>`,
        'x':              `<path d="M6 6l12 12M18 6 6 18"/>`,
        'sun':            `<circle cx="12" cy="12" r="4"/><path d="M12 2.5V5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8"/>`,
        'moon':           `<path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/>`,
        'arrow-right':    `<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>`,
        'clock':          `<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>`,
        'check-circle':   `<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>`,
        'x-circle':       `<circle cx="12" cy="12" r="9"/><path d="m9 9 6 6M15 9l-6 6"/>`,
        'alert':          `<path d="M12 3.5 2.5 20h19z"/><path d="M12 10v5M12 17.5v.5"/>`,
        'download':       `<path d="M12 4v11"/><path d="m7 11 5 5 5-5"/><path d="M5 20h14"/>`,
        'upload':         `<path d="M12 16V5"/><path d="m7 9 5-5 5 5"/><path d="M5 20h14"/>`,
        'plus':           `<path d="M12 5v14M5 12h14"/>`,
        'search':         `<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>`,
        'refresh':        `<path d="M20 11a8 8 0 0 0-14.5-4"/><path d="M5 3v4h4"/><path d="M4 13a8 8 0 0 0 14.5 4"/><path d="M19 21v-4h-4"/>`,
        'graduation':     `<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-4.5"/>`,
        'briefcase':      `<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/><path d="M3 13h18"/>`,
        'file':           `<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>`,
        'info':           `<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8v.5"/>`,
        'check':          `<path d="m5 12 5 5 9-10"/>`,
        'trash':          `<path d="M4 7h16"/><path d="M10 11v6M14 11v6"/><path d="M6 7l1 12a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2l1-12"/><path d="M9 7V4h6v3"/>`,
        'folder':         `<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>`,
    },
    svg(name, size = 18) {
        return `<svg class="icon" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><use href="#i-${name}"/></svg>`;
    },
    inject() {
        if (document.getElementById('icon-sprite') || !document.querySelector('.sidebar')) return;
        const symbols = Object.keys(this.paths).map(n => `<symbol id="i-${n}" viewBox="0 0 24 24">${this.paths[n]}</symbol>`).join('');
        document.body.insertAdjacentHTML('afterbegin', `<svg id="icon-sprite" style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true" focusable="false"><defs>${symbols}</defs></svg>`);
    },
};

const Auth = {
    login(token, user) {
        localStorage.setItem('salut_token', token);
        localStorage.setItem('salut_user', JSON.stringify(user));
        // Redirect berdasarkan role
        if (user.role === 'admin' || user.role === 'guru') {
            window.location.href = 'dashboard.html';
        } else {
            this.logout(); // role tidak diizinkan
        }
    },

    logout() {
        Api.post('/logout').catch(function() {});
        localStorage.removeItem('salut_token');
        localStorage.removeItem('salut_user');
        window.location.href = 'index.html';
    },

    user() {
        try { return JSON.parse(localStorage.getItem('salut_user')); } catch { return null; }
    },

    getUser() {
        return this.user();
    },

    /** Inisialisasi auth & guard halaman */
    init() {
        this.guard();
    },

    /** Proteksi halaman — redirect ke login jika tidak ada token */
    guard() {
        if (!localStorage.getItem('salut_token')) {
            window.location.href = 'index.html';
        }
    },

    /**
     * buildNav(activePage) — Membangun sidebar navigasi sesuai role
     * Admin: akses ke semua menu
     * Guru:  hanya Dashboard, Validasi Prestasi, Tracer Study (baca saja)
     */
    buildNav(activePage) {
        const user   = this.user();
        if (!user) return;

        const isAdmin = user.role === 'admin';

        // Update label panel
        const roleLabel = document.getElementById('sidebar-role-label');
        if (roleLabel) roleLabel.textContent = isAdmin ? 'Admin Panel' : 'Panel Guru';

        // Update user info
        const nameEl = document.getElementById('nav-user-name');
        const roleEl = document.getElementById('nav-user-role');
        const avatarEl = document.getElementById('user-avatar');
        if (nameEl)   nameEl.textContent   = user.name;
        if (roleEl)   roleEl.textContent   = user.role.charAt(0).toUpperCase() + user.role.slice(1);
        if (avatarEl) avatarEl.textContent = user.name.charAt(0).toUpperCase();

        // Daftar menu lengkap
        const allMenus = [
            {
                id: 'dashboard',
                href: 'dashboard.html',
                label: 'Dashboard',
                roles: ['admin', 'guru'],
                icon: 'dashboard',
            },
            {
                id: 'students',
                href: 'students.html',
                label: 'Siswa &amp; Alumni',
                roles: ['admin'],  // Guru TIDAK bisa lihat menu ini
                icon: 'users',
            },
            {
                id: 'rapor',
                href: 'rapor.html',
                label: 'Nilai Rapor',
                roles: ['admin', 'guru'],
                icon: 'clipboard-check',
            },
            {
                id: 'prestasi',
                href: 'prestasi.html',
                label: 'Validasi Prestasi',
                roles: ['admin', 'guru'],
                badge: 'badge-pending',
                icon: 'badge-check',
            },
            {
                id: 'arsip',
                href: 'arsip.html',
                label: 'Arsip Dokumen',
                roles: ['admin'],  // Guru TIDAK bisa upload arsip
                icon: 'archive',
            },
            {
                id: 'skills',
                href: 'skills.html',
                label: 'Portofolio Keahlian',
                roles: ['admin', 'guru'],
                icon: 'flask',
            },
            {
                id: 'tracer',
                href: 'tracer.html',
                label: 'Tracer Study',
                roles: ['admin', 'guru'],
                icon: 'chart-bar',
            },
            {
                id: 'schedules',
                href: 'schedules.html',
                label: 'Jadwal Kelulusan',
                roles: ['admin'],  // Admin only
                icon: 'calendar',
            },
        ];

        // Halaman khusus Admin yang dibuka Guru lewat URL → kembalikan ke Dashboard
        const currentMenu = allMenus.find(function(menu) { return menu.id === activePage; });
        if (currentMenu && !currentMenu.roles.includes(user.role)) {
            window.location.replace('dashboard.html');
            return;
        }

        const nav = document.getElementById('sidebar-nav');
        if (!nav) return;

        let html = '';
        allMenus.forEach(function(menu) {
            if (!menu.roles.includes(user.role)) return; // skip jika tidak diizinkan
            const active  = menu.id === activePage ? ' active' : '';
            const current = menu.id === activePage ? ' aria-current="page"' : '';
            const badge   = menu.badge ? `<span id="${menu.badge}" class="nav-count"></span>` : '';
            html += `<a href="${menu.href}" class="nav-item${active}"${current}>${Icons.svg(menu.icon)}${menu.label}${badge}</a>`;
        });

        nav.innerHTML = html;

        // Tombol logout
        const btnLogout = document.getElementById('btn-logout');
        if (btnLogout) btnLogout.addEventListener('click', function() { Auth.logout(); });
    },

    /** initNav() — Compat untuk halaman lama yang masih pakai initNav */
    initNav() {
        this.buildNav('');
    },
};

/**
 * Theme Engine — Mode Gelap / Terang. Pilihan disimpan di localStorage (salut_theme).
 * Halaman ber-topbar mendapat pemilih dua tombol; halaman tanpa topbar (login)
 * mendapat switch melayang bergaya lama.
 */
const Theme = {
    get() {
        try { return localStorage.getItem('salut_theme') || 'dark'; } catch { return 'dark'; }
    },
    set(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        try { localStorage.setItem('salut_theme', theme); } catch { /* penyimpanan tidak tersedia */ }
        this.updateButtons(theme);
        if (typeof window.onThemeChange === 'function') {
            window.onThemeChange(theme);
        }
    },
    toggle() {
        const next = this.get() === 'dark' ? 'light' : 'dark';
        this.set(next);
    },
    updateButtons(theme) {
        document.querySelectorAll('[data-theme-set]').forEach(btn => {
            btn.setAttribute('aria-pressed', String(btn.dataset.themeSet === theme));
        });
    },
    init() {
        const current = this.get();
        document.documentElement.setAttribute('data-theme', current);
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.injectHeaderButton());
        } else {
            this.injectHeaderButton();
        }
    },
    /** Pemilih tema halaman ber-topbar: dua tombol, yang aktif ditandai aria-pressed */
    buildTopbarSwitch() {
        const group = document.createElement('div');
        group.id = 'global-theme-switcher';
        group.className = 'theme-toggle';
        group.setAttribute('role', 'group');
        group.setAttribute('aria-label', 'Tema tampilan');
        [['dark', 'moon', 'Gelap'], ['light', 'sun', 'Terang']].forEach(([value, icon, label]) => {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.dataset.themeSet = value;
            btn.setAttribute('aria-label', 'Mode ' + label.toLowerCase());
            btn.innerHTML = Icons.svg(icon, 16) + '<span class="theme-label">' + label + '</span>';
            btn.addEventListener('click', () => Theme.set(value));
            group.appendChild(btn);
        });
        return group;
    },
    /** Switch melayang bergaya lama untuk halaman tanpa topbar (login) */
    buildFloatingSwitch() {
        const toggleEl = document.createElement('div');
        toggleEl.id = 'global-theme-switcher';
        toggleEl.className = 'theme-switch-control';
        toggleEl.setAttribute('role', 'button');
        toggleEl.setAttribute('tabindex', '0');
        toggleEl.setAttribute('title', 'Klik untuk beralih antara Mode Terang dan Mode Gelap');
        toggleEl.onclick = () => Theme.toggle();
        toggleEl.innerHTML = `
            <div class="theme-switch-slider"></div>
            <div class="theme-switch-opt opt-dark">
                <span class="theme-opt-icon">🌙</span>
                <span class="theme-opt-text">Gelap</span>
            </div>
            <div class="theme-switch-opt opt-light">
                <span class="theme-opt-icon">☀️</span>
                <span class="theme-opt-text">Terang</span>
            </div>
        `;
        return toggleEl;
    },
    injectHeaderButton() {
        // Hapus toggle lama jika ada
        const oldSwitcher = document.getElementById('global-theme-switcher');
        if (oldSwitcher) oldSwitcher.remove();

        const topbar = document.querySelector('.topbar');
        if (topbar) {
            // Halaman internal dengan .topbar (Dashboard, Siswa, Rapor, dll.)
            let rightSlot = topbar.querySelector('.topbar-right-slot');
            if (!rightSlot) {
                rightSlot = document.createElement('div');
                rightSlot.className = 'topbar-right-slot';

                // Pindahkan elemen bawaan (selain judul halaman) ke actions group
                const children = Array.from(topbar.children);
                const otherChildren = children.slice(1);

                if (otherChildren.length > 0) {
                    const actionsGroup = document.createElement('div');
                    actionsGroup.className = 'topbar-actions-group';
                    otherChildren.forEach(child => actionsGroup.appendChild(child));
                    rightSlot.appendChild(actionsGroup);

                    const divider = document.createElement('div');
                    divider.className = 'topbar-divider';
                    rightSlot.appendChild(divider);
                }
                topbar.appendChild(rightSlot);
            }

            let themeSlot = document.getElementById('topbar-theme-slot');
            if (!themeSlot) {
                themeSlot = document.createElement('div');
                themeSlot.id = 'topbar-theme-slot';
                rightSlot.appendChild(themeSlot);
            }
            themeSlot.innerHTML = '';
            themeSlot.appendChild(this.buildTopbarSwitch());
        } else {
            // Halaman tanpa topbar (seperti index.html Login)
            let floatWrap = document.getElementById('floating-theme-container');
            if (!floatWrap) {
                floatWrap = document.createElement('div');
                floatWrap.id = 'floating-theme-container';
                floatWrap.className = 'floating-theme-wrapper';
                document.body.appendChild(floatWrap);
            }
            floatWrap.innerHTML = '';
            floatWrap.appendChild(this.buildFloatingSwitch());
        }

        this.updateButtons(this.get());
    }
};

/**
 * Drawer — Sidebar sebagai drawer di layar <= 768px.
 * Menyuntikkan tombol hamburger ke topbar, tombol tutup ke sidebar, dan overlay gelap.
 * Ditutup lewat overlay, tombol tutup, tombol Esc, atau klik menu. Berlaku di semua halaman ber-sidebar.
 */
const Drawer = {
    mq: window.matchMedia('(max-width: 768px)'),
    sidebar: null, main: null, toggle: null, closeBtn: null, backdrop: null,

    isOpen() {
        return this.sidebar.classList.contains('is-open');
    },
    open() {
        this.sidebar.classList.add('is-open');
        this.backdrop.classList.add('show');
        document.body.classList.add('nav-open');
        this.sidebar.inert = false;
        this.main.inert = true; // fokus keyboard hanya di dalam drawer selama terbuka
        this.toggle.setAttribute('aria-expanded', 'true');
        this.toggle.setAttribute('aria-label', 'Tutup menu navigasi');
        this.closeBtn.focus();
    },
    close(returnFocus) {
        this.sidebar.classList.remove('is-open');
        this.backdrop.classList.remove('show');
        document.body.classList.remove('nav-open');
        this.main.inert = false;
        this.sidebar.inert = this.mq.matches; // drawer tertutup tidak boleh bisa difokus
        this.toggle.setAttribute('aria-expanded', 'false');
        this.toggle.setAttribute('aria-label', 'Buka menu navigasi');
        if (returnFocus) this.toggle.focus();
    },
    init() {
        this.sidebar = document.querySelector('.sidebar');
        this.main    = document.querySelector('.main');
        const topbar = document.querySelector('.topbar');
        if (!this.sidebar || !this.main || !topbar) return; // mis. halaman login

        if (!this.sidebar.id) this.sidebar.id = 'app-sidebar';

        this.toggle = document.createElement('button');
        this.toggle.type = 'button';
        this.toggle.className = 'nav-toggle';
        this.toggle.setAttribute('aria-controls', this.sidebar.id);
        this.toggle.innerHTML = Icons.svg('menu', 22);
        topbar.prepend(this.toggle);

        this.closeBtn = document.createElement('button');
        this.closeBtn.type = 'button';
        this.closeBtn.className = 'sidebar-close';
        this.closeBtn.setAttribute('aria-label', 'Tutup menu navigasi');
        this.closeBtn.innerHTML = Icons.svg('x', 18);
        const logo = this.sidebar.querySelector('.sidebar-logo');
        (logo || this.sidebar).appendChild(this.closeBtn);

        this.backdrop = document.createElement('div');
        this.backdrop.className = 'sidebar-backdrop';
        this.backdrop.setAttribute('aria-hidden', 'true');
        document.body.appendChild(this.backdrop);

        this.toggle.addEventListener('click', () => this.isOpen() ? this.close(true) : this.open());
        this.closeBtn.addEventListener('click', () => this.close(true));
        this.backdrop.addEventListener('click', () => this.close(false));
        // Menu dibangun dinamis oleh Auth.buildNav(), jadi pakai delegasi event
        this.sidebar.addEventListener('click', (e) => { if (e.target.closest('a.nav-item')) this.close(false); });
        document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && this.isOpen()) this.close(true); });
        window.addEventListener('pageshow', () => this.close(false)); // kembali via tombol Back (bfcache)
        this.mq.addEventListener('change', () => this.close(false));

        this.close(false);
    }
};

/**
 * UI — pembantu tampilan bersama halaman admin: keadaan memuat/kosong/galat dan toast.
 * Satu implementasi dipakai semua halaman (menggantikan salinan toast di tiap halaman).
 */
const UI = {
    esc(text) {
        return String(text).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
    },
    /** Kerangka tabel saat data dimuat */
    loading(rows = 6, wrap = true) {
        let html = '<span class="sr-only" role="status">Memuat data...</span>';
        for (let i = 0; i < rows; i++) {
            html += '<div class="skeleton-row" aria-hidden="true"><span class="skeleton-bar"></span><span class="skeleton-bar"></span><span class="skeleton-bar"></span></div>';
        }
        return wrap ? '<div class="table-wrap">' + html + '</div>' : html;
    },
    /** Keadaan kosong: apa yang terjadi dan apa yang bisa dilakukan berikutnya */
    empty(title, hint, icon = 'file') {
        return '<div class="empty">' + Icons.svg(icon, 32) +
            '<div class="empty-title">' + title + '</div>' +
            (hint ? '<div class="empty-sub">' + hint + '</div>' : '') + '</div>';
    },
    /** Keadaan galat: apa yang gagal dan cara mengulang (retry = ekspresi JS, mis. "loadUsers(1)") */
    error(message, retry) {
        return '<div class="empty empty-error" role="alert">' + Icons.svg('alert', 32) +
            '<div class="empty-title">Gagal memuat data</div>' +
            '<div class="empty-sub">' + UI.esc(message || 'Terjadi kesalahan. Coba lagi.') + '</div>' +
            (retry ? '<button type="button" class="btn btn-ghost btn-sm" onclick="' + retry + '">Coba lagi</button>' : '') + '</div>';
    },
    toast(msg, type = 'info') {
        const box = document.getElementById('toast-container');
        if (!box) return;
        if (!box.hasAttribute('role')) { box.setAttribute('role', 'status'); box.setAttribute('aria-live', 'polite'); }
        const el = document.createElement('div');
        el.className = 'toast toast-' + type;
        el.innerHTML = Icons.svg(type === 'success' ? 'check-circle' : type === 'error' ? 'x-circle' : 'info', 16);
        const text = document.createElement('span');
        text.textContent = msg;
        el.appendChild(text);
        box.appendChild(el);
        setTimeout(() => el.remove(), 4000);
    }
};
function toast(msg, type) { UI.toast(msg, type); }

/**
 * Modals — perilaku dialog yang sama untuk semua .modal-overlay (halaman membuka/menutup lewat kelas "show"):
 * role dialog, fokus pindah ke dalam saat terbuka, Tab berputar di dalam, Esc menutup, fokus kembali ke pemicu.
 */
const Modals = {
    FOCUSABLE: 'a[href], button:not([disabled]), input:not([disabled]):not([type="hidden"]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])',
    init() {
        document.querySelectorAll('.modal-overlay').forEach(overlay => {
            const modal = overlay.querySelector('.modal');
            if (!modal) return;
            modal.setAttribute('role', 'dialog');
            modal.setAttribute('aria-modal', 'true');
            const title = modal.querySelector('.modal-title');
            if (title) {
                title.id = title.id || overlay.id + '-title';
                modal.setAttribute('aria-labelledby', title.id);
            }
            new MutationObserver(() => {
                const open = overlay.classList.contains('show');
                if (open && !overlay._opener) {
                    overlay._opener = document.activeElement;
                    const first = modal.querySelector(this.FOCUSABLE);
                    if (first) first.focus();
                } else if (!open && overlay._opener) {
                    const opener = overlay._opener;
                    overlay._opener = null;
                    if (document.contains(opener)) opener.focus();
                }
            }).observe(overlay, { attributes: true, attributeFilter: ['class'] });
        });
        document.addEventListener('keydown', (e) => {
            const open = document.querySelector('.modal-overlay.show');
            if (!open) return;
            if (e.key === 'Escape') { open.classList.remove('show'); return; }
            if (e.key !== 'Tab') return;
            const items = Array.from(open.querySelectorAll(this.FOCUSABLE)).filter(el => el.offsetParent !== null);
            if (!items.length) return;
            const first = items[0], last = items[items.length - 1];
            if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
            else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
        });
    }
};

// Inisialisasi saat script dimuat. Urutan penting: tema membentuk slot kanan topbar dulu,
// baru sprite ikon dan tombol hamburger disuntik.
Theme.init();
if (typeof document !== 'undefined') {
    const start = () => { Icons.inject(); Drawer.init(); Modals.init(); };
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', start);
    } else {
        start();
    }
}
