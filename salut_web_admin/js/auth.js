const Auth = {
    login(token, user) {
        localStorage.setItem('salut_token', token);
        localStorage.setItem('salut_user', JSON.stringify(user));
        window.location.href = 'dashboard.html';
    },
    logout() {
        Api.post('/logout').catch(() => {});
        localStorage.removeItem('salut_token');
        localStorage.removeItem('salut_user');
        window.location.href = 'index.html';
    },
    user() {
        try { return JSON.parse(localStorage.getItem('salut_user')); } catch { return null; }
    },
    guard() {
        if (!localStorage.getItem('salut_token')) {
            window.location.href = 'index.html';
        }
    },
    initNav() {
        const user = this.user();
        if (!user) return;
        const el = document.getElementById('nav-user-name');
        if (el) el.textContent = user.name;
        const role = document.getElementById('nav-user-role');
        if (role) role.textContent = user.role.charAt(0).toUpperCase() + user.role.slice(1);
        const btn = document.getElementById('btn-logout');
        if (btn) btn.addEventListener('click', () => this.logout());
    }
};