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
        'school','class_name','jurusan','angkatan','graduation_date','is_active', 'fcm_token'
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

    /** Satu perangkat hanya menerima notifikasi untuk akun yang terakhir login di perangkat itu. */
    public function assignFcmToken(string $token): void
    {
        static::where('fcm_token', $token)->whereKeyNot($this->getKey())->update(['fcm_token' => null]);
        $this->update(['fcm_token' => $token]);
    }

    /**
     * Folder penyimpanan dokumen: angkatan_{tahun}/nisn_{nisn}.
     * Null bila angkatan/NISN tidak valid (mis. akun guru), sehingga path tidak
     * pernah terbentuk dari nilai kosong atau berisi karakter seperti "../".
     */
    public function storageFolder(): ?string
    {
        if (!preg_match('/^\d{4}$/', (string) $this->angkatan) || !preg_match('/^\d+$/', (string) $this->nisn)) {
            return null;
        }
        return "angkatan_{$this->angkatan}/nisn_{$this->nisn}";
    }

    // ─── Relationships ─────────────────────────────────────────────────────────
    public function achievements()      { return $this->hasMany(Achievement::class); }
    public function academicRecords()   { return $this->hasMany(AcademicRecord::class); }
    public function graduationDocs()    { return $this->hasMany(GraduationDoc::class); }
    public function tracerStudy()       { return $this->hasOne(TracerStudy::class); }
    public function skillCompetencies() { return $this->hasMany(\App\Models\SkillCompetency::class); }
}