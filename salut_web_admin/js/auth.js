/**
 * auth.js — Utilitas autentikasi & navigasi role-aware Web Admin SALUT
 * Mendukung role: admin (akses penuh) dan guru (akses terbatas)
 */
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
        if (roleLabel) roleLabel.textContent = isAdmin ? 'Admin Panel v1.0' : 'Panel Guru';

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
                icon: '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>',
            },
            {
                id: 'students',
                href: 'students.html',
                label: 'Siswa &amp; Alumni',
                roles: ['admin'],  // Guru TIDAK bisa lihat menu ini
                icon: '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>',
            },
            {
                id: 'rapor',
                href: 'rapor.html',
                label: 'Nilai Rapor',
                roles: ['admin', 'guru'],
                icon: '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/></svg>',
            },
            {
                id: 'prestasi',
                href: 'prestasi.html',
                label: 'Validasi Prestasi',
                roles: ['admin', 'guru'],
                badge: 'badge-pending',
                icon: '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>',
            },
            {
                id: 'arsip',
                href: 'arsip.html',
                label: 'Arsip Dokumen',
                roles: ['admin'],  // Guru TIDAK bisa upload arsip
                icon: '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"/></svg>',
            },
            {
                id: 'skills',
                href: 'skills.html',
                label: 'Portofolio Keahlian',
                roles: ['admin', 'guru'],
                icon: '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>',
            },
            {
                id: 'tracer',
                href: 'tracer.html',
                label: 'Tracer Study',
                roles: ['admin', 'guru'],
                icon: '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>',
            },
            {
                id: 'schedules',
                href: 'schedules.html',
                label: 'Jadwal Kelulusan',
                roles: ['admin'],  // Admin only
                icon: '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>',
            },
        ];

        const nav = document.getElementById('sidebar-nav');
        if (!nav) return;

        let html = '<p class="nav-label">Menu Utama</p>';
        allMenus.forEach(function(menu) {
            if (!menu.roles.includes(user.role)) return; // skip jika tidak diizinkan
            const active = menu.id === activePage ? ' active' : '';
            const badge  = menu.badge ? `<span id="${menu.badge}" style="margin-left:auto;background:rgba(245,158,11,0.2);color:#FBBF24;font-size:11px;padding:2px 8px;border-radius:20px;font-weight:700;display:none"></span>` : '';
            html += `<a href="${menu.href}" class="nav-item${active}">${menu.icon}${menu.label}${badge}</a>`;
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
 * Theme Engine — Pengatur Mode Gelap / Terang (Dark / Light)
 * Menyimpan preferensi di localStorage dan otomatis menyuntikkan switch interaktif
 * dengan posisi tetap dan tidak mengganggu elemen aksi halaman lainnya.
 */
const Theme = {
    get() {
        return localStorage.getItem('salut_theme') || 'dark';
    },
    set(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('salut_theme', theme);
        this.updateButtons(theme);
        if (typeof window !== 'undefined' && typeof window.onThemeChange === 'function') {
            window.onThemeChange(theme);
        }
    },
    toggle() {
        const next = this.get() === 'dark' ? 'light' : 'dark';
        this.set(next);
    },
    updateButtons(theme) {
        document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
            btn.innerHTML = theme === 'dark' ? '☀️ Mode Terang' : '🌙 Mode Gelap';
            btn.setAttribute('title', theme === 'dark' ? 'Beralih ke Mode Terang' : 'Beralih ke Mode Gelap');
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
    injectHeaderButton() {
        // Hapus toggle lama jika ada
        const oldSwitcher = document.getElementById('global-theme-switcher');
        if (oldSwitcher) oldSwitcher.remove();

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
            themeSlot.appendChild(toggleEl);
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
            floatWrap.appendChild(toggleEl);
        }

        this.updateButtons(this.get());
    }
};

// Jalankan auto-init tema saat script dimuat
Theme.init();
if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', () => Theme.injectHeaderButton());
}