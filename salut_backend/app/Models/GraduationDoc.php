<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Support\Facades\Storage;

/** REQ-NF-01: File path private — URL hanya digenerate melalui endpoint JWT */
class GraduationDoc extends Model
{
    use HasFactory;
    protected $fillable = ['user_id','doc_type','title','file_path','file_size','is_verified','uploaded_by'];
    protected $casts = ['is_verified' => 'boolean'];

    public function user() { return $this->belongsTo(User::class); }

    /** Cek apakah file masih ada di storage */
    public function fileExists(): bool {
        return Storage::disk('local')->exists($this->file_path);
    }
}