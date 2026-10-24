<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class TracerStudy extends Model
{
    use HasFactory;
    protected $fillable = [
        'user_id','status','nama_instansi','kota',
        'tahun_masuk','jabatan','prodi','keterangan',
        'bidang_industri','nama_kampus','nama_prodi','rentang_gaji',
    ];
    public function user() { return $this->belongsTo(User::class); }
}