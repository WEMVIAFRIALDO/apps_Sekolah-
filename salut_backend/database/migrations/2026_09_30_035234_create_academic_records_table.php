<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up(): void {
        Schema::create('academic_records', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->tinyInteger('semester')->unsigned();
            $table->decimal('average_score', 5, 2)->nullable();
            $table->integer('rank')->nullable();
            $table->year('academic_year');
            $table->enum('status', ['Tervalidasi','Draft'])->default('Draft');
            $table->foreignId('input_by')->nullable()->constrained('users')->nullOnDelete();
            $table->timestamps();
            $table->unique(['user_id','semester']);
        });
    }
    public function down(): void { Schema::dropIfExists('academic_records'); }
};