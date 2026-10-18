import 'package:flutter/material.dart';
import 'package:get/get.dart';

import 'routes/app_pages.dart';
import 'routes/app_routes.dart';

import 'package:firebase_core/firebase_core.dart';
import 'services/fcm_service.dart';
import 'services/theme_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Inisialisasi Theme Service
  Get.put(ThemeService());

  // Jalankan UI aplikasi langsung agar tidak macet/freeze di logo!
  runApp(const SalutApp());

  // Inisialisasi Firebase & FCM secara non-blocking di background
  _initServicesAsync();
}

Future<void> _initServicesAsync() async {
  try {
    await Firebase.initializeApp().timeout(const Duration(seconds: 3));
    Get.putAsync(() => FcmService().init());
  } catch (e) {
    debugPrint("Firebase background info: $e");
  }
}

class SalutApp extends StatelessWidget {
  const SalutApp({super.key});

  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      title: 'SALUT App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF1E3A5F)),
        useMaterial3: true,
        fontFamily: 'Roboto',
      ),
      // ── Routing GetX: Dimulai dari Splash Screen 3 Detik ─────────────
      initialRoute: AppRoutes.splash,
      getPages: AppPages.routes,
    );
  }
}
