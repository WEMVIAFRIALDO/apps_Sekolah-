<?php

namespace App\Console\Commands;

use App\Services\FcmService;
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

    public function handle(FcmService $fcm)
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

            $lulusan = \App\Models\User::where('role', 'siswa')
                ->where('angkatan', $schedule->angkatan)
                // Pastikan yang lulus hanya kelas XII, jika data mensyaratkan itu
                ->where('class_name', 'like', 'XII %');

            $tokens = (clone $lulusan)->whereNotNull('fcm_token')->pluck('fcm_token')->all();
            $updated = $lulusan->update(['role' => 'alumni']);

            $schedule->update(['status' => 'completed']);
            $this->info("Berhasil mengubah {$updated} siswa angkatan {$schedule->angkatan} menjadi alumni.");

            $terkirim = $fcm->send(
                $tokens,
                'Selamat, kamu telah lulus',
                'Status akunmu kini Alumni. Buka SALUT untuk melihat arsip dokumen dan mengisi tracer study.'
            );
            $this->info("Notifikasi terkirim ke {$terkirim} dari " . count($tokens) . ' perangkat terdaftar.');
        }
        
        $this->info('Proses kelulusan selesai.');
    }
}
