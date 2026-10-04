<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;

class PromoteAlumni extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'salut:promote-alumni';
    protected $description = 'Otomatis mengubah status siswa kelas XII menjadi alumni berdasarkan jadwal kelulusan (REQ-F-07)';

    public function handle()
    {
        $this->info('Mengecek jadwal kelulusan...');
        
        $schedules = \App\Models\GraduationSchedule::where('status', 'pending')
            ->where('graduation_date', '<=', now())
            ->get();

        if ($schedules->isEmpty()) {
            $this->info('Tidak ada jadwal kelulusan yang jatuh tempo.');
            return;
        }

        foreach ($schedules as $schedule) {
            $this->info("Memproses kelulusan angkatan {$schedule->angkatan}...");

            $updated = \App\Models\User::where('role', 'siswa')
                ->where('angkatan', $schedule->angkatan)
                // Pastikan yang lulus hanya kelas XII, jika data mensyaratkan itu
                ->where('class_name', 'like', 'XII %')
                ->update(['role' => 'alumni']);

            $schedule->update(['status' => 'completed']);
            $this->info("Berhasil mengubah {$updated} siswa angkatan {$schedule->angkatan} menjadi alumni.");
        }
        
        $this->info('Proses kelulusan selesai.');
    }
}
