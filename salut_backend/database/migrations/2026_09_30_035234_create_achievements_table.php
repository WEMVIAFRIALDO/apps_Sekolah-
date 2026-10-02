<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

/** REQ-NF-03: Prestasi siswa dengan status validasi guru */
return new class extends Migration {
    public function up(): void {
        Schema::create('achievements', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->string('nama_kegiatan');
            $table->string('penyelenggara');
            $table->enum('tingkat', ['Kecamatan / Kabupaten','Kota / Madya','Provinsi','Nasional','Internasional']);
            $table->string('peringkat');
            $table->year('tahun');
            $table->text('deskripsi')->nullable();
            $table->enum('status_validasi', ['Pending','Approved','Rejected'])->default('Pending');
            $table->string('sertifikat_path')->nullable(); // path relatif dari storage/app/public
            $table->text('catatan')->nullable();           // catatan dari guru saat reject
            $table->foreignId('validated_by')->nullable()->constrained('users')->nullOnDelete();
            $table->timestamp('validated_at')->nullable();
            $table->timestamps();
        });
    }
    public function down(): void { Schema::dropIfExists('achievements'); }
};