import 'package:flutter/material.dart';
import 'package:get/get.dart';

import 'routes/app_pages.dart';
import 'routes/app_routes.dart';

import 'package:firebase_core/firebase_core.dart';
import 'services/fcm_service.dart';
import 'services/theme_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Inisialisasi Firebase
  await Firebase.initializeApp();
  
  // Inisialisasi Theme Service
  Get.put(ThemeService());

  // Inisialisasi FCM Service menggunakan GetX
  await Get.putAsync(() => FcmService().init());

  runApp(const SalutApp());
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
