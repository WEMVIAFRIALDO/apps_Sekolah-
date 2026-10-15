import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:get/get.dart';
import 'package:flutter/material.dart';

@pragma('vm:entry-point')
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  await Firebase.initializeApp();
  debugPrint("Handling a background message: ${message.messageId}");
}

class FcmService extends GetxService {
  final FirebaseMessaging _fcm = FirebaseMessaging.instance;

  Future<FcmService> init() async {
    // 1. Setup Background Handler
    FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);

    // 2. Request Permission (untuk iOS & Android 13+)
    NotificationSettings settings = await _fcm.requestPermission(
      alert: true,
      badge: true,
      sound: true,
    );
    debugPrint('User granted permission: ${settings.authorizationStatus}');

    // 3. Dapatkan FCM Token (Opsional, bisa dikirim ke server nanti)
    try {
      String? token = await _fcm.getToken();
      debugPrint("FCM Token: $token");
    } catch (e) {
      debugPrint("Gagal mengambil FCM Token: $e");
    }

    // 4. Listener saat app berjalan di foreground
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      debugPrint('Got a message whilst in the foreground!');
      debugPrint('Message data: ${message.data}');

      if (message.notification != null) {
        // Tampilkan Snackbar / Alert kustom di dalam app
        Get.snackbar(
          message.notification!.title ?? 'Notifikasi Baru',
          message.notification!.body ?? '',
          snackPosition: SnackPosition.TOP,
          backgroundColor: Colors.blueAccent.withValues(alpha: 0.9),
          colorText: Colors.white,
          margin: const EdgeInsets.all(15),
          duration: const Duration(seconds: 5),
          icon: const Icon(Icons.notifications_active, color: Colors.white),
        );
      }
    });

    // 5. Listener saat app dibuka dari notifikasi (background -> foreground)
    FirebaseMessaging.onMessageOpenedApp.listen((RemoteMessage message) {
      debugPrint('A new onMessageOpenedApp event was published!');
    });

    return this;
  }
}
