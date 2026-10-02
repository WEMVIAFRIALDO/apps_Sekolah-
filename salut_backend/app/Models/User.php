<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Tymon\JWTAuth\Contracts\JWTSubject;

/**
 * REQ-NF-02: Model User dengan multi-role dan JWT support.
 */
class User extends Authenticatable implements JWTSubject
{
    use HasFactory, Notifiable;

    protected $fillable = [
        'name','email','password','nisn','role','phone',
        'school','class_name','angkatan','graduation_date','is_active',
    ];

    protected $hidden = ['password','remember_token'];

    protected $casts = [
        'email_verified_at' => 'datetime',
        'graduation_date'   => 'date',
        'is_active'         => 'boolean',
        'angkatan'          => 'integer',
    ];

    // ─── JWT Interface ─────────────────────────────────────────────────────────
    public function getJWTIdentifier() { return $this->getKey(); }
    public function getJWTCustomClaims(): array { return []; }

    // ─── Role Helpers ──────────────────────────────────────────────────────────
    public function isSiswa(): bool  { return $this->role === 'siswa'; }
    public function isAlumni(): bool { return $this->role === 'alumni'; }
    public function isGuru(): bool   { return $this->role === 'guru'; }
    public function isAdmin(): bool  { return $this->role === 'admin'; }

    // ─── Relationships ─────────────────────────────────────────────────────────
    public function achievements()   { return $this->hasMany(Achievement::class); }
    public function academicRecords(){ return $this->hasMany(AcademicRecord::class); }
    public function graduationDocs() { return $this->hasMany(GraduationDoc::class); }
    public function tracerStudy()    { return $this->hasOne(TracerStudy::class); }
}