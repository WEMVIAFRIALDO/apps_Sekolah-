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
    ];
    public function user() { return $this->belongsTo(User::class); }
}