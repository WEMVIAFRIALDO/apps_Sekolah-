const API_BASE = 'http://localhost:8000/api';

const Api = {
    token: () => localStorage.getItem('salut_token'),

    headers() {
        const h = { 'Content-Type': 'application/json', 'Accept': 'application/json' };
        if (this.token()) h['Authorization'] = `Bearer ${this.token()}`;
        return h;
    },

    async request(method, path, body = null) {
        const opts = { method, headers: this.headers() };
        if (body) opts.body = JSON.stringify(body);
        const res = await fetch(`${API_BASE}${path}`, opts);
        const json = await res.json();
        if (res.status === 401) { Auth.logout(); return; }
        if (!res.ok) throw json;
        return json;
    },

    get:    (path)        => Api.request('GET',   path),
    post:   (path, body)  => Api.request('POST',  path, body),
    patch:  (path, body)  => Api.request('PATCH', path, body),

    async upload(path, formData) {
        const headers = { 'Accept': 'application/json' };
        if (this.token()) headers['Authorization'] = `Bearer ${this.token()}`;
        const res = await fetch(`${API_BASE}${path}`, { method: 'POST', headers, body: formData });
        const json = await res.json();
        if (!res.ok) throw json;
        return json;
    }
};