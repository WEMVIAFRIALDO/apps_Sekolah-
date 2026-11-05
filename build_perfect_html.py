# -*- coding: utf-8 -*-
"""
Script Pembangun File Preview HTML Sesuai Standar Format Contoh Makalah Unila:
- Font: Times New Roman 12pt
- Warna: Hitam Murni (RGB: 0, 0, 0), bebas font biru
- Bab: Center Bold
- Subbab: Left Bold (tidak rata kanan-kiri)
- Paragraf: Justified
- Lampiran II: Kotak Template Screenshot Pengguna
Penulis: Wemvi Afrialdo
"""

import os

ROOT_DIR = r"d:\proyek_applikasi"
BASE_DIR = r"d:\proyek_applikasi\apps_sekolah"

def get_base_css(title):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Times New Roman', Times, serif;
            font-size: 12pt;
            background: #E4E4E7;
            color: #000000;
            line-height: 1.5;
            padding: 40px 20px;
        }}
        .page {{
            max-width: 820px;
            margin: 0 auto 30px;
            background: #FFFFFF;
            border: 1px solid #D4D4D8;
            padding: 70px 80px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.08);
            position: relative;
            min-height: 1100px;
        }}
        .cover-box {{
            text-align: center;
            padding-top: 40px;
        }}
        .univ-title {{
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            text-transform: uppercase;
            line-height: 1.3;
        }}
        .doc-title {{
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            margin: 24px 0 6px;
            line-height: 1.35;
            text-transform: uppercase;
        }}
        .doc-subtitle {{
            font-size: 12pt;
            color: #000000;
            font-style: italic;
            margin-bottom: 30px;
        }}
        .logo-box {{
            text-align: center;
            margin: 30px 0;
        }}
        .logo-box img {{
            width: 170px;
            height: auto;
        }}
        .meta-group {{
            margin: 20px 0;
            font-size: 12pt;
            color: #000000;
            line-height: 1.4;
        }}
        .meta-group strong {{
            font-weight: bold;
        }}
        .bottom-univ {{
            margin-top: 40px;
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            text-transform: uppercase;
            line-height: 1.25;
        }}
        .bab-title {{
            text-align: center;
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            text-transform: uppercase;
            margin: 20px 0 16px;
            line-height: 1.3;
        }}
        h2.subbab {{
            text-align: left !important;
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            margin: 20px 0 6px;
        }}
        h3.sub-subbab {{
            text-align: left !important;
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            margin: 14px 0 4px;
        }}
        p {{
            font-size: 12pt;
            color: #000000;
            margin-bottom: 12px;
            text-align: justify;
            line-height: 1.5;
            text-indent: 0.35in;
        }}
        p.no-indent {{
            text-indent: 0 !important;
        }}
        .figure-box {{
            text-align: center;
            margin: 14px 0 20px;
        }}
        .figure-box img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #D4D4D8;
        }}
        .figure-box.mobile img {{
            max-width: 280px;
        }}
        .caption-top {{
            text-align: center;
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            margin-bottom: 6px;
        }}
        .placeholder-box {{
            border: 2px dashed #000000;
            background: #FAFAFA;
            border-radius: 4px;
            padding: 30px 20px;
            text-align: center;
            margin: 14px 0 24px;
        }}
        .placeholder-box .p-title {{
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            margin-bottom: 4px;
        }}
        .placeholder-box .p-sub {{
            font-size: 11pt;
            font-style: italic;
            color: #000000;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 11pt;
            margin: 16px 0 24px;
        }}
        th, td {{
            padding: 8px 10px;
            border: 1px solid #000000;
            color: #000000;
        }}
        th {{
            background: #E5E7EB;
            font-weight: bold;
            text-align: center;
        }}
        .toc-row {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 4px;
            font-size: 12pt;
        }}
        .toc-title {{
            flex-shrink: 0;
        }}
        .toc-dots {{
            flex-grow: 1;
            border-bottom: 1px dotted #000000;
            margin: 0 6px 4px;
        }}
        .toc-page {{
            flex-shrink: 0;
            font-weight: bold;
        }}
        .btn-print {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #000000;
            color: #FFFFFF;
            padding: 12px 20px;
            border-radius: 4px;
            font-size: 12pt;
            font-family: 'Times New Roman', serif;
            font-weight: bold;
            border: none;
            cursor: pointer;
            z-index: 100;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }}
        .page-num {{
            text-align: center;
            margin-top: 30px;
            font-size: 12pt;
        }}
        @media print {{
            body {{ padding: 0; background: #FFF; }}
            .page {{ box-shadow: none; border: none; padding: 0; margin-bottom: 0; page-break-after: always; }}
            .btn-print {{ display: none; }}
        }}
    </style>
</head>
<body>
<button class="btn-print" onclick="window.print()">🖨️ Cetak / Simpan PDF</button>
"""

def generate_perfect_html_instalasi():
    title = "Laporan Instalasi Toolchain & Server SALUT"
    h = get_base_css(title)
    h += """
    <div class="page">
        <div class="cover-box">
            <div class="doc-title">LAPORAN INSTALASI DAN KONFIGURASI TOOLCHAIN<br>PENGEMBANGAN APLIKASI MOBILE DAN SERVER SISTEM SALUT</div>
            <div class="doc-subtitle">Disusun untuk memenuhi tugas Matakuliah Pengembangan Aplikasi Mobile</div>
            <div class="logo-box"><img src="laporan_screenshots/instalasi/logo_unila.png" alt="Logo Unila"></div>
            <div class="meta-group">
                <strong>Dosen Mata Kuliah :</strong><br>
                Ghea Chandra Surawan, M.Pd.
            </div>
            <div class="meta-group">
                <strong>Disusun Oleh:</strong><br>
                Wemvi Afrialdo (2413025052)
            </div>
            <div class="meta-group">
                <strong>Tautan Repositori GitHub:</strong><br>
                <u>https://github.com/WEMVIAFRIALDO/apps_Sekolah-</u>
            </div>
            <div class="bottom-univ">
                PROGRAM STUDI PENDIDIKAN TEKNOLOGI INFORMASI<br>
                JURUSAN PENDIDIKAN MATEMATIKA DAN ILMU PENGETAHUAN ALAM<br>
                FAKULTAS KEGURUAN DAN ILMU PENDIDIKAN<br>
                UNIVERSITAS LAMPUNG<br>
                2026
            </div>
        </div>
    </div>

    <div class="page">
        <div class="bab-title">KATA PENGANTAR</div>
        <p>Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat dan karunia-Nya, sehingga Laporan Teknis Instalasi dan Konfigurasi Toolchain Pengembangan Aplikasi Mobile SALUT ini dapat diselesaikan dengan baik dan tepat waktu.</p>
        <p>Laporan ini mendokumentasikan tahapan fundamental dalam penyiapan lingkungan pengembangan, mencakup pemasangan Flutter SDK, Dart, Java Development Kit (JDK 21 LTS), Android Studio, Android SDK Command-line Tools, CMake, NDK, editor Visual Studio Code, hingga konfigurasi server lokal XAMPP dan framework Laravel 12.</p>
        <p>Ucapan terima kasih penulis sampaikan kepada Bapak Dosen Pengampu serta rekan-rekan mahasiswa yang telah memberikan bimbingan dan masukan konstruktif dalam penyelesaian instalasi ini. Semoga laporan ini bermanfaat bagi pembaca.</p>
        <div style="text-align: right; margin-top: 40px;">
            Bandar Lampung, 19 Oktober 2026<br>
            Penyusun,<br><br><br>
            <strong>Wemvi Afrialdo</strong><br>
            NPM. 2413025052
        </div>
        <div class="page-num">i</div>
    </div>

    <div class="page">
        <div class="bab-title">BAB I<br>PENDAHULUAN</div>
        <h2 class="subbab">1.1 Latar Belakang Penyiapan Lingkungan</h2>
        <p>Keberhasilan pembangunan aplikasi lintas platform (cross-platform mobile) berakar pada kesiapan toolchain dan rantai kompilasi yang kokoh. Pengembangan sistem informasi SALUT (Sistem Arsip Kelulusan dan Tracer Study Alumni SMK) memerlukan integrasi antara frontend mobile berbasis Flutter dan backend server berbasis PHP Laravel 12 dengan basis data relasional MySQL. Oleh karena itu, penyiapan lingkungan pengembangan yang presisi menjadi prasyarat mutlak sebelum tahap perancangan logika bisnis dimulai.</p>
        
        <h2 class="subbab">1.2 Tujuan Penyiapan Toolchain</h2>
        <p class="no-indent">Tujuan dari penyiapan lingkungan instalasi ini adalah:<br>
        1. Mengunduh dan mengonfigurasi Flutter SDK versi stabil dan Dart SDK pada sistem operasi Windows.<br>
        2. Mengonfigurasi Java Development Kit (JDK 21 LTS) dan Android SDK Command-line Tools untuk kompilasi APK.<br>
        3. Mempersiapkan IDE Visual Studio Code beserta ekstensi pendukung rekayasa Flutter.<br>
        4. Memastikan seluruh dependensi berstatus siap pakai melalui verifikasi flutter doctor tanpa kesalahan.<br>
        5. Menyiapkan web server lokal XAMPP dan framework Laravel 12 sebagai fondasi RESTful API.</p>

        <h2 class="subbab">1.3 Manfaat Praktis</h2>
        <p>Manfaat penyiapan lingkungan ini adalah tersedianya ekosistem pengkodean yang stabil, mendukung proses kompilasi cepat (hot-reload), dan memudahkan deployment aplikasi secara mandiri baik pada emulator maupun perangkat fisik Android.</p>
        <div class="page-num">1</div>
    </div>

    <div class="page">
        <div class="bab-title">BAB II<br>LAPORAN INSTALASI TOOLCHAIN & SERVER</div>
        <p class="no-indent">Bab ini menguraikan tahapan teknis pelaksanaan instalasi lingkungan pengembangan aplikasi SALUT secara berurutan, dimulai dari pengunduhan paket resmi Flutter, konfigurasi variabel sistem, penyiapan Android SDK, hingga verifikasi diagnosa.</p>
        
        <h2 class="subbab">2.1 Persiapan Lingkungan dan Pengunduhan Flutter SDK</h2>
        <div class="caption-top">Gambar 2.1. Halaman Pengunduhan Flutter SDK dari Portal Resmi flutter.dev</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step01_flutter_website.png" alt="Portal Flutter"></div>
        <p>Gambar 2.1 memperlihatkan halaman pengunduhan resmi Flutter SDK pada peramban web. Pengembang mengunduh bundel kompilasi stabil untuk sistem operasi Windows guna memperoleh pustaka inti antarmuka grafis dan Dart compiler.</p>

        <div class="caption-top">Gambar 2.2. Berkas Arsip Terkompresi Flutter SDK pada Folder Unduhan</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step02_download_flutter_zip.png" alt="Zip Flutter"></div>
        <p>Gambar 2.2 mendokumentasikan berkas arsip zip Flutter SDK yang telah berhasil diunduh. Berkas ini kemudian diekstrak ke direktori penyimpanan lokal tanpa spasi.</p>
        <div class="page-num">3</div>
    </div>

    <div class="page">
        <h2 class="subbab">2.2 Ekstraksi Berkas dan Konfigurasi Environment Variables PATH</h2>
        <div class="caption-top">Gambar 2.3. Konfigurasi Variabel Lingkungan Sistem (System Environment Variables)</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step03_environment_variables.png" alt="PATH Windows"></div>
        <p>Gambar 2.3 menunjukkan jendela konfigurasi Environment Variables pada Windows. Jalur direktori flutter\\bin ditambahkan ke variabel PATH sistem agar perintah terminal flutter dan dart dapat dipanggil secara global dari sesi terminal mana pun.</p>

        <div class="caption-top">Gambar 2.4. Verifikasi Versi Flutter SDK dan Dart pada Terminal Command Prompt</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step04_flutter_version_cmd.png" alt="Flutter Version CMD"></div>
        <p>Gambar 2.4 membuktikan keberhasilan pengenalan perintah flutter --version pada command prompt, yang menampilkan rincian rilis Flutter Channel stable beserta versi Dart SDK yang menyertainya.</p>
        <div class="page-num">4</div>
    </div>

    <div class="page">
        <h2 class="subbab">2.3 Instalasi dan Konfigurasi Java Development Kit (JDK 21)</h2>
        <div class="caption-top">Gambar 2.5. Berkas Instalasi Java Development Kit 21 (JDK 21 LTS)</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step05_download_jdk21.png" alt="JDK 21 Installer"></div>
        <p>Gambar 2.5 menampilkan berkas pemasangan Java Development Kit (JDK 21 LTS). JDK 21 diperlukan oleh Gradle untuk memproses kompilasi kode Kotlin dan Java pada layer platform Android.</p>

        <div class="caption-top">Gambar 2.6. Verifikasi Java Runtime Environment dan JAVA_HOME</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step06_java_version_terminal.png" alt="Java Version"></div>
        <p>Gambar 2.6 memvalidasi eksekusi java -version yang mengonfirmasi bahwa OpenJDK 64-Bit Server VM telah aktif dengan benar di sistem.</p>
        <div class="page-num">5</div>
    </div>

    <div class="page">
        <h2 class="subbab">2.4 Instalasi Ekstensi Flutter dan Dart pada Visual Studio Code</h2>
        <div class="caption-top">Gambar 2.7. Instalasi Ekstensi Resmi Flutter pada Marketplace VS Code</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step07_vscode_flutter_extension.png" alt="Ekstensi Flutter"></div>
        <p>Gambar 2.7 memperlihatkan pemasangan ekstensi Flutter pada Visual Studio Code. Ekstensi ini menyediakan fitur code completion, hot reload, widget tree inspection, dan debugging langsung.</p>

        <div class="caption-top">Gambar 2.8. Instalasi Ekstensi Bahasa Dart pada Visual Studio Code</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step08_vscode_dart_extension.png" alt="Ekstensi Dart"></div>
        <p>Gambar 2.8 mendokumentasikan ekstensi bahasa Dart yang memberikan dukungan linter dan analisis statis kode aplikasi.</p>
        <div class="page-num">6</div>
    </div>

    <div class="page">
        <h2 class="subbab">2.5 Konfigurasi Android Studio, SDK Tools, dan CMake</h2>
        <div class="caption-top">Gambar 2.9. Pengaturan Android SDK Command-line Tools dan CMake</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step09_android_sdk_tools_cmake.png" alt="SDK Manager"></div>
        <p>Gambar 2.9 menampilkan panel Android SDK Manager. Dipasang komponen Android SDK Command-line Tools (latest) dan CMake guna menjamin kesiapan toolchain kompilasi native C/C++ pada pustaka tertentu.</p>

        <div class="caption-top">Gambar 2.10. Status Pemasangan Android NDK pada SDK Tools</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step10_android_ndk_installed.png" alt="Android NDK"></div>
        <p>Gambar 2.10 memverifikasi status pemasangan Android NDK (Side by side) yang diperlukan untuk proses linking kode native Android.</p>
        <div class="page-num">7</div>
    </div>

    <div class="page">
        <h2 class="subbab">2.6 Pengujian Kelayakan Toolchain dengan Flutter Doctor</h2>
        <div class="caption-top">Gambar 2.11. Hasil Diagnosa Menyeluruh Perintah flutter doctor</div>
        <div class="figure-box"><img src="laporan_screenshots/instalasi/step11_flutter_doctor_output.png" alt="Flutter Doctor OK"></div>
        <p>Gambar 2.11 menampilkan laporan diagnosa flutter doctor yang mengonfirmasi bahwa seluruh komponen vital: Flutter SDK, Android toolchain (licenses accepted), Android Studio, VS Code, dan perangkat terhubung (connected device) telah berstatus centang hijau (No issues found!).</p>

        <div class="bab-title" style="margin-top: 40px;">BAB III<br>PENUTUP</div>
        <h2 class="subbab">3.1 Kesimpulan Instalasi</h2>
        <p>Seluruh rangkaian tahapan instalasi dan konfigurasi toolchain untuk pengembangan aplikasi SALUT telah berhasil diselesaikan dengan baik. Sistem operasi Windows telah terkonfigurasi dengan Flutter SDK, Dart, JDK 21, Android SDK Tools, VS Code IDE, dan XAMPP Server. Hasil diagnosa flutter doctor membuktikan tidak ada kendala dependensi sehingga lingkungan pengembangan siap digunakan untuk perancangan aplikasi.</p>
        <div class="page-num">8</div>
    </div>
</body>
</html>
"""
    with open(os.path.join(ROOT_DIR, "Laporan_Instalasi.html"), "w", encoding="utf-8") as f:
        f.write(h)
    with open(os.path.join(BASE_DIR, "Laporan_Instalasi.html"), "w", encoding="utf-8") as f:
        f.write(h)
    print("Selesai Laporan_Instalasi.html")

def generate_perfect_html_laporan_akhir():
    title = "Laporan Akhir Pengembangan Sistem SALUT - Wemvi Afrialdo"
    h = get_base_css(title)
    h += """
    <div class="page">
        <div class="cover-box">
            <div class="doc-title">LAPORAN AKHIR PENGEMBANGAN SISTEM INFORMASI ARSIP KELULUSAN DAN TRACER STUDY ALUMNI SMK (SALUT)</div>
            <div class="doc-subtitle">Disusun untuk memenuhi tugas Matakuliah Pengembangan Aplikasi Mobile</div>
            <div class="logo-box"><img src="laporan_screenshots/instalasi/logo_unila.png" alt="Logo Unila"></div>
            <div class="meta-group">
                <strong>Dosen Mata Kuliah :</strong><br>
                Ghea Chandra Surawan, M.Pd.
            </div>
            <div class="meta-group">
                <strong>Disusun Oleh:</strong><br>
                Wemvi Afrialdo (2413025052)
            </div>
            <div class="meta-group">
                <strong>Tautan Repositori GitHub:</strong><br>
                <u>https://github.com/WEMVIAFRIALDO/apps_Sekolah-</u>
            </div>
            <div class="bottom-univ">
                PROGRAM STUDI PENDIDIKAN TEKNOLOGI INFORMASI<br>
                JURUSAN PENDIDIKAN MATEMATIKA DAN ILMU PENGETAHUAN ALAM<br>
                FAKULTAS KEGURUAN DAN ILMU PENDIDIKAN<br>
                UNIVERSITAS LAMPUNG<br>
                2026
            </div>
        </div>
    </div>

    <div class="page">
        <div class="bab-title">KATA PENGANTAR</div>
        <p>Puji dan syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas segala limpahan rahmat, hidayah, dan karunia-Nya, sehingga Laporan Komprehensif Perancangan, Instalasi, dan Pengembangan Sistem Informasi Arsip Kelulusan dan Tracer Study Alumni SMK (SALUT) ini dapat diselesaikan dengan baik dan tepat waktu.</p>
        <p>Laporan ini disusun sebagai bentuk pertanggungjawaban akademis sekaligus pemenuhan tugas akhir dalam mata kuliah Pengembangan Aplikasi Mobile pada Program Studi Pendidikan Teknologi Informasi, Jurusan Pendidikan MIPA, Fakultas Keguruan dan Ilmu Pendidikan, Universitas Lampung. Laporan ini mendokumentasikan pilar utama pengembangan: perancangan spesifikasi kebutuhan dan mockup antarmuka (SRS), laporan teknis instalasi dan konfigurasi toolchain pengembangan, arsitektur backend RESTful API Laravel 12 dan MySQL, antarmuka mobile Flutter dengan Dynamic UI Rendering, integrasi portofolio kejuruan SMK (SKPI), otomatisasi kelulusan berbasis cron job dan Push Notification Firebase, linimasa progres proyek, hingga prototype antarmuka sistem untuk semua peran pengguna.</p>
        <p>Ucapan terima kasih yang setinggi-tingginya penulis sampaikan kepada Bapak Ghea Chandra Surawan, M.Pd., selaku Dosen Pengampu mata kuliah Pengembangan Aplikasi Mobile, Bapak dan Ibu Dosen Program Studi PTIK FKIP Universitas Lampung, serta rekan-rekan mahasiswa angkatan 2024 atas arahan, motivasi, dan bantuan teknis selama proses pengembangan.</p>
        <div style="text-align: right; margin-top: 40px;">
            Bandar Lampung, 19 Oktober 2026<br>
            Penyusun,<br><br><br>
            <strong>Wemvi Afrialdo</strong><br>
            NPM. 2413025052
        </div>
        <div class="page-num">i</div>
    </div>

    <div class="page">
        <div class="bab-title">DAFTAR ISI</div>
        <div class="toc-row"><strong>HALAMAN JUDUL</strong><div class="toc-dots"></div><div class="toc-page"></div></div>
        <div class="toc-row"><strong>KATA PENGANTAR</strong><div class="toc-dots"></div><div class="toc-page">i</div></div>
        <div class="toc-row"><strong>DAFTAR ISI</strong><div class="toc-dots"></div><div class="toc-page">ii</div></div>
        <div class="toc-row"><strong>BAB I PENDAHULUAN</strong><div class="toc-dots"></div><div class="toc-page">1</div></div>
        <div class="toc-row">&nbsp;&nbsp;1.1 Latar Belakang<div class="toc-dots"></div><div class="toc-page">1</div></div>
        <div class="toc-row">&nbsp;&nbsp;1.2 Rumusan Masalah<div class="toc-dots"></div><div class="toc-page">1</div></div>
        <div class="toc-row">&nbsp;&nbsp;1.3 Tujuan Pengembangan<div class="toc-dots"></div><div class="toc-page">2</div></div>
        <div class="toc-row">&nbsp;&nbsp;1.4 Manfaat Pengembangan<div class="toc-dots"></div><div class="toc-page">2</div></div>
        <div class="toc-row"><strong>BAB II LAPORAN INSTALASI TOOLCHAIN & SERVER</strong><div class="toc-dots"></div><div class="toc-page">3</div></div>
        <div class="toc-row">&nbsp;&nbsp;2.1 Persiapan Lingkungan dan Pengunduhan Flutter SDK<div class="toc-dots"></div><div class="toc-page">3</div></div>
        <div class="toc-row">&nbsp;&nbsp;2.2 Ekstraksi Berkas dan Konfigurasi Environment Variables PATH<div class="toc-dots"></div><div class="toc-page">4</div></div>
        <div class="toc-row">&nbsp;&nbsp;2.3 Instalasi dan Konfigurasi Java Development Kit (JDK 21)<div class="toc-dots"></div><div class="toc-page">5</div></div>
        <div class="toc-row">&nbsp;&nbsp;2.4 Instalasi Ekstensi Flutter dan Dart pada Visual Studio Code<div class="toc-dots"></div><div class="toc-page">6</div></div>
        <div class="toc-row">&nbsp;&nbsp;2.5 Konfigurasi Android Studio, SDK Tools, dan CMake<div class="toc-dots"></div><div class="toc-page">7</div></div>
        <div class="toc-row">&nbsp;&nbsp;2.6 Pengujian Kelayakan Toolchain dengan Flutter Doctor<div class="toc-dots"></div><div class="toc-page">8</div></div>
        <div class="toc-row"><strong>BAB III PEMBAHASAN PENGEMBANGAN SISTEM SALUT</strong><div class="toc-dots"></div><div class="toc-page">9</div></div>
        <div class="toc-row">&nbsp;&nbsp;3.1 Perancangan Desain Sistem dan Mockup UI (Laporan 1)<div class="toc-dots"></div><div class="toc-page">9</div></div>
        <div class="toc-row">&nbsp;&nbsp;3.2 Pengembangan Backend RESTful API dan Database (Laporan Perkembangan 1)<div class="toc-dots"></div><div class="toc-page">11</div></div>
        <div class="toc-row">&nbsp;&nbsp;3.3 Pengembangan Antarmuka Mobile Flutter dan Dynamic UI (Laporan Perkembangan 2)<div class="toc-dots"></div><div class="toc-page">13</div></div>
        <div class="toc-row">&nbsp;&nbsp;3.4 Pengembangan Fitur Kejuruan SMK dan Portofolio SKPI (Laporan Perkembangan 3)<div class="toc-dots"></div><div class="toc-page">15</div></div>
        <div class="toc-row">&nbsp;&nbsp;3.5 Integrasi Push Notification, Otomasi Cron, dan Tracer Study (Laporan Perkembangan 4)<div class="toc-dots"></div><div class="toc-page">17</div></div>
        <div class="toc-row"><strong>BAB IV PENUTUP</strong><div class="toc-dots"></div><div class="toc-page">19</div></div>
        <div class="toc-row">&nbsp;&nbsp;4.1 Kesimpulan<div class="toc-dots"></div><div class="toc-page">19</div></div>
        <div class="toc-row">&nbsp;&nbsp;4.2 Saran<div class="toc-dots"></div><div class="toc-page">20</div></div>
        <div class="toc-row"><strong>LAMPIRAN</strong><div class="toc-dots"></div><div class="toc-page">21</div></div>
        <div class="toc-row">&nbsp;&nbsp;Lampiran I: Tabel Progres Mingguan Pengembangan Sistem SALUT<div class="toc-dots"></div><div class="toc-page">21</div></div>
        <div class="toc-row">&nbsp;&nbsp;Lampiran II: Dokumentasi Screenshot Antarmuka Pengguna Seluruh Role (Admin, Guru, Siswa, Alumni)<div class="toc-dots"></div><div class="toc-page">23</div></div>
        <div class="page-num">ii</div>
    </div>

    <div class="page">
        <div class="bab-title">LAMPIRAN II<br>DOKUMENTASI SCREENSHOT ANTARMUKA PENGGUNA SELURUH ROLE<br>(ADMINISTRATOR, GURU, SISWA AKTIF, ALUMNI)</div>
        <p>Bagian ini disediakan secara khusus sebagai lembar kerja dokumentasi visual tangkapan layar langsung (screenshot) yang diambil oleh pengembang dari perangkat uji coba aktual. Disediakan kotak templat resmi bergaris batas presisi untuk seluruh 4 aktor sistem SALUT:</p>

        <h3 class="sub-subbab">1. DOKUMENTASI ANTARMUKA ROLE ADMINISTRATOR (WEB ADMIN PANEL)</h3>
        <div class="caption-top">Gambar L.1. Dasbor Statistik & Analitik Kejuruan SMK (Role Admin)</div>
        <div class="placeholder-box">
            <div class="p-title">📷 [AREA TEMPEL SCREENSHOT PENGGUNA]</div>
            <div class="p-sub">Tempelkan tangkapan layar dasbor analitik keterserapan alumni, sebaran jurusan, dan metrik sistem.</div>
        </div>

        <div class="caption-top">Gambar L.2. Manajemen Master Data Siswa & Alumni (Role Admin)</div>
        <div class="placeholder-box">
            <div class="p-title">📷 [AREA TEMPEL SCREENSHOT PENGGUNA]</div>
            <div class="p-sub">Tempelkan tangkapan layar tabel data siswa, filter kelas/angkatan, dan fitur Import CSV.</div>
        </div>

        <div class="caption-top">Gambar L.3. Pengelolaan Arsip Dokumen Digital Ijazah & SKL (Role Admin)</div>
        <div class="placeholder-box">
            <div class="p-title">📷 [AREA TEMPEL SCREENSHOT PENGGUNA]</div>
            <div class="p-sub">Tempelkan tangkapan layar verifikasi berkas ijazah sah dan modal unggah dokumen alumni.</div>
        </div>

        <h3 class="sub-subbab">2. DOKUMENTASI ANTARMUKA ROLE GURU (WEB ADMIN PANEL)</h3>
        <div class="caption-top">Gambar L.6. Modul Penginputan Nilai Rapor Siswa Per Semester (Role Guru)</div>
        <div class="placeholder-box">
            <div class="p-title">📷 [AREA TEMPEL SCREENSHOT PENGGUNA]</div>
            <div class="p-sub">Tempelkan tangkapan layar tabel input nilai mata pelajaran per semester siswa.</div>
        </div>

        <h3 class="sub-subbab">3. DOKUMENTASI ANTARMUKA ROLE SISWA AKTIF (MOBILE FLUTTER APP)</h3>
        <div class="caption-top">Gambar L.8. Halaman Splash Screen & Autentikasi Login Siswa (Role Siswa)</div>
        <div class="placeholder-box">
            <div class="p-title">📷 [AREA TEMPEL SCREENSHOT PENGGUNA]</div>
            <div class="p-sub">Tempelkan tangkapan layar tampilan splash screen 3 detik dan form login pada HP Samsung Anda.</div>
        </div>

        <div class="caption-top">Gambar L.9. Halaman Dasbor Utama Siswa Aktif (Role Siswa)</div>
        <div class="placeholder-box">
            <div class="p-title">📷 [AREA TEMPEL SCREENSHOT PENGGUNA]</div>
            <div class="p-sub">Tempelkan tangkapan layar beranda siswa aktif berisi kartu profil, banner SKPI, dan riwayat prestasi.</div>
        </div>

        <h3 class="sub-subbab">4. DOKUMENTASI ANTARMUKA ROLE ALUMNI (MOBILE FLUTTER APP)</h3>
        <div class="caption-top">Gambar L.12. Halaman Dasbor Utama Alumni (Role Alumni)</div>
        <div class="placeholder-box">
            <div class="p-title">📷 [AREA TEMPEL SCREENSHOT PENGGUNA]</div>
            <div class="p-sub">Tempelkan tangkapan layar beranda alumni dengan status kelulusan dan menu tracer study di HP Samsung.</div>
        </div>

        <div class="caption-top">Gambar L.13. Modul Arsip Digital Kelulusan Ijazah & SKL Sah Ber-TTE (Role Alumni)</div>
        <div class="placeholder-box">
            <div class="p-title">📷 [AREA TEMPEL SCREENSHOT PENGGUNA]</div>
            <div class="p-sub">Tempelkan tangkapan layar daftar unduhan berkas PDF Ijazah Asli dan SKL terverifikasi.</div>
        </div>
        <div class="page-num">25</div>
    </div>
</body>
</html>
"""
    with open(os.path.join(ROOT_DIR, "Laporan_Akhir_Lengkap.html"), "w", encoding="utf-8") as f:
        f.write(h)
    with open(os.path.join(BASE_DIR, "Laporan_Akhir_Lengkap.html"), "w", encoding="utf-8") as f:
        f.write(h)
    print("Selesai Laporan_Akhir_Lengkap.html")

if __name__ == "__main__":
    generate_perfect_html_instalasi()
    generate_perfect_html_laporan_akhir()
    print("HTML preview sempurna selesai dibuat!")
