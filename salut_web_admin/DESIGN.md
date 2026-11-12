# DESIGN.md: Tampilan Web Admin SALUT (8 halaman di balik login)

Status: **Opsi C diterapkan di 8 halaman** (dashboard, students, arsip, rapor, skills, prestasi, tracer, schedules). Struktur dan komponen Opsi A, palet navy/cyan dari versi lama. `css/style.css` sudah dipangkas hanya untuk halaman login. Backup sementara ada di `_backup_ui/` (menunggu keputusan penghapusan).

## 1. Riwayat keputusan

1. Dua opsi diusulkan: **A "Basalt"** (basal gelap + amethyst, selaras gambar login) dan **B "Kertas & Pinus"** (terang, hijau pinus).
2. Dipilih A dengan syarat datar (tanpa glow, gradien, blur kaca). Fondasi dan dashboard dibangun.
3. Setelah melihat hasilnya, arah diubah: pengguna lebih suka suasana warna **lama** (navy gelap, biru/cyan) yang dekat dengan login dan logo, dengan **susunan dan komponen baru** dipertahankan. Hasilnya **Opsi C**: yang diganti hanya nilai token palet dan font judul; struktur HTML/CSS komponen tidak berubah.

Alasan Opsi C: palet navy/biru/cyan sudah akrab bagi guru dan admin, menyatu dengan logo SALUT dan halaman login, sementara susunan baru (hierarki dashboard, ikon SVG, tabel rapat) menyelesaikan masalah keterbacaan yang menjadi alasan rombak.

## 2. Masalah di versi lama (alasan rombak, tetap berlaku)

| Temuan | Bukti |
|---|---|
| Bentuk dan bobot seragam, glow, kaca buram | `style.css`: 10 `backdrop-filter`, 10 gradien, `--primary-glow`, radius 18-24px di hampir semua kartu |
| Emoji sebagai ikon | 92 emoji di 8 halaman |
| Gaya tersebar di HTML | 292 atribut `style="..."`, warna heksa mentah |
| Komponen didefinisikan ulang | `arsip.html` mendefinisikan ulang `.stat-card`, `.stat-icon`, `.stat-grid` |
| Variabel belum terdefinisi | `--orange` (dashboard) dan `--surface` (arsip) dipakai tanpa definisi |
| Dashboard tanpa hierarki | 5 kartu statistik identik; "Prestasi Pending" tidak lebih menonjol |

## 3. Palet Opsi C (nilai ada di token `css/app.css`, satu-satunya tempat)

Prinsip: setiap warna lama diturunkan menjadi **warna solid** (bukan rgba bertingkat yang meniru kaca). Latar `#0A0F1D` dan permukaan `#111827` adalah nilai lama (`--navy-bg`, dan rgba(17,24,39) tanpa transparansi). Aksen biru `#3B82F6`/`#2563EB` dan cyan `#06B6D4` adalah nilai lama; slate untuk teks sekunder juga nilai lama (login memakai slate yang sama).

### Mode gelap (bawaan)

| Token | Nilai | Pasangan | Rasio |
|---|---|---|---|
| `--bg` | `#0A0F1D` | `--text` `#F8FAFC` di atasnya | 18,26 |
| `--surface` | `#111827` | `--text` | 16,96 |
| | | `--text-muted` `#94A3B8` | 6,92 |
| | | `--accent` `#60A5FA` (teks, tautan, ikon aktif) | 6,98 |
| | | `--cyan` `#06B6D4` | 7,31 |
| `--surface-raised` | `#1E293B` | `--text` / muted / accent / cyan | 13,98 / 5,71 / 5,75 / 6,03 |
| Tombol utama | latar `--accent-fill` `#2563EB`, teks `#FFFFFF` | | 5,17 (hover `#1D4ED8`: 6,70) |
| Badge siswa | `--accent` di atas `--accent-tint` `#192B4C` | | 5,54 |
| Badge alumni | `--cyan` di atas `--cyan-tint` `#0F3143` | | 5,61 |
| Badge sukses | `--ok` `#34D399` di atas `#12312F` | | 7,25 |
| Badge menunggu | `--warn` `#F59E0B` di atas `#312B23` | | 6,52 |
| Badge ditolak | `--danger` `#F87171` di atas `#312431` | | 5,32 |
| Garis non-teks | fokus `--accent` di atas bg / surface | | 7,52 / 6,98 (min 3) |
| | tombol `#2563EB` di atas surface | | 3,43 (min 3) |

### Mode terang

| Token | Nilai | Pasangan | Rasio |
|---|---|---|---|
| `--bg` | `#F8FAFC` | `--text` `#0F172A` | 17,06 |
| `--surface` | `#FFFFFF` | `--text` | 17,85 |
| | | `--text-muted` `#526277` | 6,23 (di atas `--surface-raised` `#F1F5F9`: 5,68) |
| | | `--accent` `#2563EB` | 5,17 (di atas raised: 4,72) |
| | | `--cyan` `#0E7490` | 5,36 |
| Tombol utama | latar `#2563EB`, teks `#FFFFFF` | | 5,17 (hover `#1D4ED8`: 6,70) |
| Badge siswa | `#2563EB` di atas `#EAF1FE` | | 4,56 |
| Badge alumni | `#0E7490` di atas `#D6F3F9` | | 4,60 |
| Badge sukses | `#047857` di atas `#DCF5EA` | | 4,78 |
| Badge menunggu | `#B45309` di atas `#FFF6DC` | | 4,66 |
| Badge ditolak | `#B91C1C` di atas `#FDE4E4` | | 5,36 |

Hasil perhitungan: **0 pasangan gagal** (batas teks 4,5; non-teks 3,0) di kedua mode. Diverifikasi dua cara: dari token (skrip hitung WCAG) dan dari DOM yang benar-benar dirender (82 teks pada dashboard di mode gelap dan terang, 0 di bawah batas).

### Warna grafik

Aturan: satu warna aksen untuk data utama, abu-abu slate untuk sisanya, warna status hanya jika kategorinya memang harus dibedakan.

| Grafik | Warna |
|---|---|
| Siswa per jurusan, daftar kampus | biru (`--chart-1`) |
| Daftar industri | cyan (`--chart-2`) |
| Distribusi pengguna | siswa biru; alumni dan guru slate (`--chart-6` dan `--chart-7`) |
| Status alumni (tracer) | **tetap dibedakan**: bekerja biru, kuliah cyan, wirausaha amber, mencari kerja merah, belum memutuskan slate (lima kategori dengan legenda teks; tidak bisa disederhanakan tanpa kehilangan keterbacaan) |
| Status prestasi | **tetap dibedakan**: pending amber, approved hijau |

Semua warna grafik >= 3:1 terhadap permukaan (terendah: slate gelap 3,73; slate kedua terang 3,42).

## 4. Font

| Peran | Font | Dipakai di |
|---|---|---|
| Judul besar (>= 16px) | **Plus Jakarta Sans** 600 | judul halaman, judul bagian, judul modal (sama dengan login) |
| Teks, tabel, form, tombol, menu, judul kartu | **IBM Plex Sans** 400/500/600 | semua yang lain |
| Angka, NISN, kode | **IBM Plex Mono** 400/500 | KPI, jumlah, NISN, nomor peringkat |

Alasan (diuji dengan merender tabel contoh berisi data asli di kedua font): di tabel padat 13px, **Plex Sans lebih terbaca**: spasi antar-kata lega, angka "1" tegas, dan semua baris muat satu baris. Plus Jakarta Sans memiliki spasi kata rapat dan huruf lebar, membuat 2 dari 5 baris membungkus (nama institusi dan kelas), tabel 3% lebih tinggi, dan "X TKJ 1" terbaca "XTKJ1". Pada ukuran judul besar kekurangan itu tidak terlihat dan ciri khasnya menyatukan dashboard dengan halaman login. Judul kartu 14px awalnya memakai Jakarta, tetapi spasi katanya menempel di layar sungguhan, maka dikembalikan ke Plex Sans.

## 5. Aturan yang dipegang

- **Datar:** 0 `backdrop-filter`, 0 gradien, 0 glow, 0 `!important`, 0 emoji di `app.css` dan dashboard. Bayangan hanya pada lapisan melayang (modal, drawer, toast). Overlay modal/drawer berupa scrim solid tanpa blur.
- **Token tunggal:** tidak ada heksa/rgba di luar blok token. Nilai diubah di tempat asalnya; tidak ada file CSS baru untuk Opsi C.
- **Login dilindungi:** `index.html` dan gambar login tidak disentuh; screenshot sebelum/sesudah selisih 0 piksel (375px dan 1440px). `css/style.css` tetap utuh sampai pembersihan akhir.
- **Struktur dipertahankan:** hierarki dashboard (blok "Prestasi menunggu validasi" paling menonjol, deretan angka rapat), ikon SVG satu sprite, tabel rapat + badge teks, state kosong/memuat/galat, hamburger/drawer, mode gelap/terang dengan localStorage.
- Skala: spasi basis 4px; radius menurut peran (tag 4, kontrol 6, kartu 8, modal 12); tipografi dasar 14px, tabel 13px, batas bawah 12px.
- Gerak (Motion vanilla, `motion@12.23.12`): hanya masuk halaman dan angka statistik naik; baris tabel dan modal menyusul bersama halamannya. Dilewati bila `prefers-reduced-motion`.

## 6. Bagian palet lama yang tidak bisa dipertahankan (jujur)

| Bagian lama | Alasan diganti | Penggantinya |
|---|---|---|
| Gradien tombol/aksen, gradien latar `radial-gradient`, glow `--primary-glow` | melanggar aturan datar | warna solid; tombol `#2563EB` |
| Lapisan rgba bertingkat (`--navy-surface` .85, `--navy-card` .78, `--border` .10, `--input-bg` .85) | meniru kaca | warna solid hasil perataan di atas latar navy |
| Teks putih di atas biru `#3B82F6` (tombol utama) | rasio 3,68, gagal AA | latar tombol `#2563EB` (5,17); `#3B82F6` tetap dipakai untuk grafik (4,82) |
| Cyan neon `#00F2FE` dan indigo `#6366F1`/`#818CF8` dari login | neon butuh glow; indigo termasuk ungu yang diminta diganti | cyan solid `#06B6D4`, biru |
| Mode terang lama: cyan `#0284C7` (4,10), emerald `#059669` (3,77), amber `#D97706` (3,19) sebagai teks | gagal AA di atas putih | `#0E7490` (5,36), `#047857` (5,48), `#B45309` (5,02) |
| Mode terang lama: muted `#64748B` di atas `#F1F5F9` (4,34) | gagal AA | `#526277` (5,68) |
| Garis lama putih 10% (hasil perataan `#292F3D`, abu-abu netral) | tidak ada versi solid yang sekaligus bernuansa navy | `#263248`, navy yang lebih biru dari aslinya (keputusan estetika) |
| Teks `--muted-dim` `#64748B` pada latar gelap (3,73) | gagal AA sebagai teks | tidak dipakai sebagai teks; dipakai hanya untuk grafik (>= 3) |

## 7. Rencana teknis

### 7.1 Struktur CSS

- `css/style.css`: dipakai halaman login; belum diubah. Di akhir dibersihkan sehingga hanya berisi yang dipakai `index.html`, dan aturan lama yang tidak dipakai 8 halaman dihapus dengan bukti grep dan screenshot login identik.
- `css/app.css`: token + seluruh komponen tema baru. 8 halaman memuatnya sebagai ganti `style.css`.
- Berkas JS pendukung: `js/theme-init.js` (tema tersimpan diterapkan di `<head>`), `js/motion.js` (gerak), perubahan `js/auth.js` (sprite ikon, menu, pemilih tema, drawer).

### 7.2 Urutan kerja

1. Fondasi + `dashboard.html`: **selesai**.
2. 7 halaman lain: **selesai**. Tiap halaman diuji (data tampil, form tersimpan, console bersih, 375px dan 1440px, kontras DOM).
3. Pembersihan `style.css`: **selesai** (23.269 menjadi 4.389 byte; 32 keadaan login identik 0 piksel). Komponen yang dulu didefinisikan ulang di `arsip.html` kini ada di `app.css`; variabel `--surface`, `--orange`, `--red` yatim sudah tidak dipakai. Berikutnya: keputusan penghapusan `_backup_ui/`.

### 7.3 Keterbatasan

- **MCP 21st.dev tidak aktif di sesi ini**; referensi pola dari skill `ui-ux-pro-max` dan `frontend-design`.
- `../AGENTS.md` tidak ada; yang ada `apps_sekolah/AGENTS.md` (menyebut Tailwind padahal web admin memakai CSS biasa; kode yang diikuti).
