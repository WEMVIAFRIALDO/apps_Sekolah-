<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

/**
 * SMK Upgrade: Tabel skill_competencies untuk mencatat Kompetensi/Skill yang dikuasai siswa.
 * Menjadi dasar SKPI (Surat Keterangan Pendamping Ijazah) / Portofolio Alumni.
 *
 * Relasi: user (siswa/alumni) memiliki banyak skill_competencies.
 */
return new class extends Migration {
    public function up(): void {
        Schema::create('skill_competencies', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();

            // Nama skill/kompetensi spesifik sesuai jurusan
            // Contoh TKJ: "Konfigurasi Router MikroTik", "Instalasi Jaringan LAN"
            // Contoh RPL: "Desain UI/UX Figma", "Pemrograman Web dengan Laravel"
            $table->string('nama_kompetensi');

            // Kategori/bidang skill (sesuai mapel kejuruan)
            $table->string('kategori')->nullable(); // misal: Jaringan, Pemrograman, Desain Grafis

            // Level penguasaan
            $table->enum('level', ['Dasar', 'Terampil', 'Mahir'])->default('Dasar');

            // Keterangan atau deskripsi tambahan dari guru
            $table->text('keterangan')->nullable();

            // Guru yang menginput
            $table->foreignId('guru_id')->nullable()->constrained('users')->nullOnDelete();

            // Semester & tahun pelajaran saat skill dinilai
            $table->string('semester', 10)->nullable(); // "Ganjil" / "Genap"
            $table->string('tahun_pelajaran', 10)->nullable(); // "2025/2026"

            $table->timestamps();
        });
    }

    public function down(): void {
        Schema::dropIfExists('skill_competencies');
    }
};
