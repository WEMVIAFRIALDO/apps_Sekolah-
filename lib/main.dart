import 'package:flutter/material.dart';
import 'package:get/get.dart';

import 'routes/app_pages.dart';
import 'routes/app_routes.dart';

void main() {
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
      // ── Routing GetX ──────────────────────────────────────────────────
      initialRoute: AppRoutes.login,
      getPages: AppPages.routes,
    );
  }
}
