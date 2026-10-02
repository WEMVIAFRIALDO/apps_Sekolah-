<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

/** REQ-NF-02: Multi-role support (admin, guru, siswa, alumni) */
return new class extends Migration {
    public function up(): void {
        Schema::table('users', function (Blueprint $table) {
            $table->string('nisn', 10)->unique()->nullable()->after('id');
            $table->enum('role', ['admin', 'guru', 'siswa', 'alumni'])->default('siswa')->after('email');
            $table->string('phone', 20)->nullable()->after('role');
            $table->string('school')->default('SMA Negeri 1 Teladan')->after('phone');
            $table->string('class_name', 20)->nullable()->after('school');
            $table->year('angkatan')->nullable()->after('class_name');
            $table->date('graduation_date')->nullable()->after('angkatan');
            $table->boolean('is_active')->default(true)->after('graduation_date');
        });
    }
    public function down(): void {
        Schema::table('users', function (Blueprint $table) {
            $table->dropColumn(['nisn','role','phone','school','class_name','angkatan','graduation_date','is_active']);
        });
    }
};