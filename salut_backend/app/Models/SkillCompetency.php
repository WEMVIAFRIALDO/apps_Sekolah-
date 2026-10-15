<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

/**
 * Model SkillCompetency — Portofolio / SKPI Siswa SMK.
 * Relasi: User (siswa/alumni) memiliki banyak kompetensi yang diinput Guru.
 */
class SkillCompetency extends Model
{
    use HasFactory;

    protected $fillable = [
        'user_id',
        'guru_id',
        'nama_kompetensi',
        'kategori',
        'level',
        'keterangan',
        'semester',
        'tahun_pelajaran',
    ];

    // ─── Relationships ──────────────────────────────────────────────────────────
    public function siswa()  { return $this->belongsTo(User::class, 'user_id'); }
    public function guru()   { return $this->belongsTo(User::class, 'guru_id'); }
}
