<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class Achievement extends Model
{
    use HasFactory;

    protected $fillable = [
        'user_id','nama_kegiatan','penyelenggara','tingkat','peringkat',
        'tahun','deskripsi','status_validasi','sertifikat_path','catatan',
        'validated_by','validated_at',
    ];

    protected $casts = ['validated_at' => 'datetime'];

    public function user()      { return $this->belongsTo(User::class); }
    public function validator() { return $this->belongsTo(User::class, 'validated_by'); }

    public function isApproved(): bool { return $this->status_validasi === 'Approved'; }
    public function isPending(): bool  { return $this->status_validasi === 'Pending'; }
}