<?php

require __DIR__ . '/vendor/autoload.php';
$app = require_once __DIR__ . '/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

use App\Models\GraduationSchedule;

$schedules = [
    [
        'angkatan' => 2024,
        'graduation_date' => '2024-05-06 09:00:00',
        'status' => 'completed',
    ],
    [
        'angkatan' => 2025,
        'graduation_date' => '2025-05-05 09:00:00',
        'status' => 'completed',
    ],
    [
        'angkatan' => 2026,
        'graduation_date' => '2026-05-04 10:00:00',
        'status' => 'pending',
    ],
    [
        'angkatan' => 2027,
        'graduation_date' => '2027-05-03 10:00:00',
        'status' => 'pending',
    ],
];

foreach ($schedules as $s) {
    GraduationSchedule::updateOrCreate(
        ['angkatan' => $s['angkatan']],
        ['graduation_date' => $s['graduation_date'], 'status' => $s['status']]
    );
}

echo "BERHASIL: " . GraduationSchedule::count() . " jadwal kelulusan tersimpan di database.\n";
