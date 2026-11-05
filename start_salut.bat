@echo off
setlocal
title SALUT - Starter

set "ROOT=%~dp0"
set "BACKEND=%ROOT%salut_backend"
set "WEB_ADMIN=%ROOT%salut_web_admin\index.html"
set "PHP_EXE=C:\xampp\php\php.exe"
if not exist "%PHP_EXE%" set "PHP_EXE=php"
if not defined SALUT_PORT set "SALUT_PORT=8000"

echo [1/4] Mengecek MySQL di port 3306...
call :port_aktif 3306
if errorlevel 1 (
    echo [GAGAL] MySQL tidak aktif di port 3306. Nyalakan MySQL dari XAMPP Control Panel, lalu jalankan ulang.
    pause
    exit /b 1
)
echo       MySQL aktif.

echo [2/4] Menjalankan backend di port %SALUT_PORT%...
call :port_aktif %SALUT_PORT%
if errorlevel 1 (
    start "SALUT Backend" /D "%BACKEND%" cmd /k ""%PHP_EXE%" artisan serve --port=%SALUT_PORT%"
) else (
    echo       Port %SALUT_PORT% sudah dipakai, server baru tidak dijalankan.
)

echo [3/4] Menjalankan penjadwal...
"%SystemRoot%\System32\tasklist.exe" /v /fi "WINDOWTITLE eq SALUT Scheduler*" | "%SystemRoot%\System32\find.exe" /i "cmd.exe" >nul
if errorlevel 1 (
    start "SALUT Scheduler" /D "%BACKEND%" cmd /k ""%PHP_EXE%" artisan schedule:work"
) else (
    echo       Penjadwal sudah berjalan.
)

echo [4/4] Membuka Web Admin...
start "" "%WEB_ADMIN%"

echo Selesai. Tutup jendela "SALUT Backend" dan "SALUT Scheduler" untuk menghentikan layanan.
exit /b 0

:port_aktif
powershell -NoProfile -Command "$c = New-Object Net.Sockets.TcpClient; try { $c.Connect('127.0.0.1', %1); exit 0 } catch { exit 1 }" >nul 2>&1
exit /b %errorlevel%
