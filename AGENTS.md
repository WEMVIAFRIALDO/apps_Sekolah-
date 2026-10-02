**Konteks Proyek:** SALUT (Sistem Arsip Lulusan & Tracer Study) menggunakan arsitektur Client-Server.

**Tech Stack Utama:** Frontend Mobile (Flutter Android), Frontend Web (HTML, Tailwind CSS, JavaScript), Backend API (Laravel PHP), dan Database (MySQL/TiDB).

**Aturan Keamanan:** Semua komunikasi API dan tautan akses dokumen rahasia (Rapor, SKL, SKHUN, Ijazah) mutlak membutuhkan autentikasi JWT (Bearer Token).

**Aturan Mobile (Flutter):**

- Wajib menerapkan Dynamic UI Rendering; komponen visual dan menu harus berubah secara real-time berdasarkan role pengguna (Siswa Aktif atau Alumni) sesaat setelah login.
- Optimalkan struktur kode dan aset agar ukuran akhir APK dibatasi maksimal 120MB dan dapat berjalan minimal di Android 8.0 (Oreo).
- Buat antarmuka kuesioner Tracer Study menggunakan form dinamis yang field-nya bertambah sesuai pilihan status pengguna.

**Aturan Backend (Laravel):**

- Bangun tabel basis data yang mendukung multi-role (Admin, Guru, Siswa Aktif, Alumni).
- Atur penyimpanan cloud storage secara hierarkis berdasarkan angkatan dan NISN (contoh: angkatan_2026/nisn_12345/ijazah.pdf).
- Siapkan cron job di latar belakang untuk mengeksekusi trigger transisi otomatis role Siswa menjadi Alumni saat jadwal pengumuman tiba.
