<?php
use App\Http\Controllers\Api\AdminController;
use App\Http\Controllers\Api\ArsipController;
use App\Http\Controllers\Api\AuthController;
use App\Http\Controllers\Api\PrestasiController;
use App\Http\Controllers\Api\ProfileController;
use App\Http\Controllers\Api\TracerStudyController;
use Illuminate\Support\Facades\Route;

// ─── Public Routes (tidak perlu JWT) ─────────────────────────────────────────
Route::post('/login',   [AuthController::class, 'login']);

// ─── Protected Routes (wajib JWT Bearer Token) ───────────────────────────────
Route::middleware('jwt.auth')->group(function () {
    Route::post('/logout',  [AuthController::class, 'logout']);
    Route::post('/refresh', [AuthController::class, 'refresh']);

    // Profil
    Route::prefix('profile')->group(function () {
        Route::get('/',           [ProfileController::class, 'show']);
        Route::patch('/',         [ProfileController::class, 'update']);
        Route::patch('/password', [ProfileController::class, 'changePassword']);
    });

    // Prestasi Siswa (REQ-F-03, REQ-NF-03)
    Route::prefix('prestasi')->group(function () {
        Route::get('/',                          [PrestasiController::class, 'index']);
        Route::post('/',                         [PrestasiController::class, 'store']);
        Route::get('/{achievement}/sertifikat',  [PrestasiController::class, 'downloadSertifikat']);
    });

    // Arsip Digital Alumni (REQ-F-06, REQ-NF-01)
    Route::prefix('arsip')->group(function () {
        Route::get('/',                            [ArsipController::class, 'index']);
        Route::post('/',                           [ArsipController::class, 'store']);
        Route::get('/{graduationDoc}/download',    [ArsipController::class, 'download']);
    });

    // Tracer Study (REQ-F-08)
    Route::prefix('tracer-study')->group(function () {
        Route::get('/',  [TracerStudyController::class, 'show']);
        Route::post('/', [TracerStudyController::class, 'store']);
    });

    // Admin & Guru Panel
    Route::prefix('admin')->group(function () {
        Route::get('/stats',                                    [AdminController::class, 'stats']);
        // Manajemen Pengguna (REQ-F-02)
        Route::get('/users',                                    [AdminController::class, 'listUsers']);
        Route::post('/users',                                   [AdminController::class, 'createUser']);
        Route::patch('/users/{user}/promote',                   [AdminController::class, 'promoteToAlumni']);
        // Validasi Prestasi (REQ-F-04)
        Route::get('/achievements',                             [AdminController::class, 'listAchievements']);
        Route::patch('/achievements/{achievement}/validate',    [AdminController::class, 'validateAchievement']);
        // Tracer Study Rekapitulasi (REQ-F-10)
        Route::get('/tracer-studies',                          [AdminController::class, 'listTracerStudies']);
        Route::get('/tracer-studies/export-csv',               [AdminController::class, 'exportTracerCsv']);
        // Jadwal Kelulusan (REQ-F-07)
        Route::get('/schedules',                               [AdminController::class, 'listSchedules']);
        Route::post('/schedules',                              [AdminController::class, 'createSchedule']);
    });
});