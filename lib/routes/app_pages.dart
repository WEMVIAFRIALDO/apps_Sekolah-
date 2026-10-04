import 'package:get/get.dart';

import '../pages/login_page.dart';
import '../pages/dashboard_page.dart';
import '../pages/prestasi_page.dart';
import '../pages/tracer_page.dart';
import '../pages/profile_page.dart';
import '../pages/arsip_page.dart';

import '../controllers/dashboard_controller.dart';
import '../controllers/prestasi_controller.dart';
import '../controllers/tracer_controller.dart';
import '../controllers/profile_controller.dart';

import 'app_routes.dart';

/// Mendaftarkan seluruh halaman beserta binding controller-nya.
/// Binding memastikan controller di-inject tepat saat halaman diakses,
/// dan di-dispose otomatis saat halaman ditutup (memory-efficient).
abstract class AppPages {
  AppPages._();

  static final routes = <GetPage>[
    GetPage(
      name: AppRoutes.login,
      page: () => const LoginPage(),
      transition: Transition.fadeIn,
    ),
    GetPage(
      name: AppRoutes.dashboard,
      page: () => const DashboardPage(),
      binding: BindingsBuilder(() {
        Get.lazyPut<DashboardController>(() => DashboardController());
      }),
      transition: Transition.rightToLeft,
    ),
    GetPage(
      name: AppRoutes.prestasi,
      page: () => const PrestasiPage(),
      binding: BindingsBuilder(() {
        Get.lazyPut<PrestasiController>(() => PrestasiController());
      }),
      transition: Transition.rightToLeft,
    ),
    GetPage(
      name: AppRoutes.tracer,
      page: () => const TracerPage(),
      binding: BindingsBuilder(() {
        Get.lazyPut<TracerController>(() => TracerController());
      }),
      transition: Transition.rightToLeft,
    ),
    GetPage(
      name: AppRoutes.profile,
      page: () => const ProfilePage(),
      binding: BindingsBuilder(() {
        Get.lazyPut<ProfileController>(() => ProfileController());
      }),
      transition: Transition.rightToLeft,
    ),
    // REQ-F-09: Halaman Arsip Dokumen Alumni
    GetPage(
      name: AppRoutes.arsip,
      page: () => const ArsipPage(),
      transition: Transition.rightToLeft,
    ),
  ];
}
