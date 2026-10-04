<?php

use Illuminate\Foundation\Inspiring;
use Illuminate\Support\Facades\Artisan;

Artisan::command('inspire', function () {
    $this->comment(Inspiring::quote());
})->purpose('Display an inspiring quote');

// REQ-F-07: Cron job untuk transisi otomatis Siswa menjadi Alumni
use Illuminate\Support\Facades\Schedule;

Schedule::command('salut:promote-alumni')->dailyAt('00:00');
