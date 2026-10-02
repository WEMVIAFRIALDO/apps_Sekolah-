<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class AcademicRecord extends Model
{
    use HasFactory;
    protected $fillable = ['user_id','semester','average_score','rank','academic_year','status','input_by'];
    public function user() { return $this->belongsTo(User::class); }
}