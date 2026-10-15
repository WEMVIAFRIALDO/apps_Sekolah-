<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

/**
 * SMK Upgrade: Tambahkan kolom detail Tracer Study untuk statistik sebaran lulusan.
 * - Untuk yang Bekerja: nama_perusahaan_detail, bidang_industri
 * - Untuk yang Kuliah: nama_kampus, nama_prodi
 */
return new class extends Migration {
    public function up(): void {
        Schema::table('tracer_studies', function (Blueprint $table) {
            // Detail untuk status "Bekerja" / "Wirausaha"
            $table->string('bidang_industri')->nullable()->after('jabatan');
            // Catatan: nama_instansi sudah ada, digunakan untuk nama perusahaan/kampus

            // Detail untuk status "Kuliah / Melanjutkan Studi"
            $table->string('nama_kampus')->nullable()->after('bidang_industri');
            $table->string('nama_prodi')->nullable()->after('nama_kampus');

            // Gaji / Pendapatan (opsional, untuk riset)
            $table->string('rentang_gaji')->nullable()->after('nama_prodi');
            // contoh: "< 2 Juta", "2-5 Juta", "> 5 Juta"
        });
    }

    public function down(): void {
        Schema::table('tracer_studies', function (Blueprint $table) {
            $table->dropColumn(['bidang_industri', 'nama_kampus', 'nama_prodi', 'rentang_gaji']);
        });
    }
};

