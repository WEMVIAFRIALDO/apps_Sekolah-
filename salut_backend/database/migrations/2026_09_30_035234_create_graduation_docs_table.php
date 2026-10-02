<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

/**
 * REQ-F-06: Arsip digital (Ijazah, SKHUN, SKL, Rapor).
 * REQ-NF-01: file_path bersifat PRIVATE — wajib JWT untuk akses.
 * Storage hierarkis: angkatan_{year}/nisn_{nisn}/{doc_type}.pdf
 */
return new class extends Migration {
    public function up(): void {
        Schema::create('graduation_docs', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->enum('doc_type', ['ijazah','skhun','skl','rapor','portofolio']);
            $table->string('title');
            $table->string('file_path');   // private storage path
            $table->string('file_size')->nullable();
            $table->boolean('is_verified')->default(true);
            $table->foreignId('uploaded_by')->nullable()->constrained('users')->nullOnDelete();
            $table->timestamps();
        });
    }
    public function down(): void { Schema::dropIfExists('graduation_docs'); }
};