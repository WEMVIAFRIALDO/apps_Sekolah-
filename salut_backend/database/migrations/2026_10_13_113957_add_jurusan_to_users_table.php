<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

/**
 * SMK Upgrade: Tambahkan kolom jurusan (Program Keahlian) ke tabel users.
 * Contoh nilai: TKJ, RPL, Multimedia, Akuntansi, dll.
 */
return new class extends Migration {
    public function up(): void {
        Schema::table('users', function (Blueprint $table) {
            $table->string('jurusan')->nullable()->after('class_name');
        });
    }

    public function down(): void {
        Schema::table('users', function (Blueprint $table) {
            $table->dropColumn('jurusan');
        });
    }
};

