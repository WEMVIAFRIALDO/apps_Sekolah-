/// Konstanta nama rute untuk seluruh halaman di aplikasi SALUT.
/// Semua navigasi menggunakan Get.toNamed() / Get.offAllNamed()
/// dengan referensi ke konstanta di sini agar tidak ada typo.
abstract class AppRoutes {
  AppRoutes._();

  static const login     = '/login';
  static const dashboard = '/dashboard';
  static const prestasi  = '/prestasi';
  static const tracer    = '/tracer';
  static const profile   = '/profile';
}
