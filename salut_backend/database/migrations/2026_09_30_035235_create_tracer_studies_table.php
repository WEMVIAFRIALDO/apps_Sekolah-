<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

/** REQ-F-08: Form dinamis Tracer Study Alumni pasca-lulus */
return new class extends Migration {
    public function up(): void {
        Schema::create('tracer_studies', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->string('status');             // Bekerja, Kuliah, Wirausaha, dll
            $table->string('nama_instansi')->nullable();
            $table->string('kota')->nullable();
            $table->string('tahun_masuk', 4)->nullable();
            $table->string('jabatan')->nullable();  // field kondisional: Bekerja/Wirausaha
            $table->string('prodi')->nullable();    // field kondisional: Kuliah
            $table->text('keterangan')->nullable();
            $table->timestamps();
        });
    }
    public function down(): void { Schema::dropIfExists('tracer_studies'); }
};