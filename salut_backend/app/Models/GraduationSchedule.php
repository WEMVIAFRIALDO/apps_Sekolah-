<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class GraduationSchedule extends Model
{
    protected $fillable = ['angkatan', 'graduation_date', 'status'];
}
