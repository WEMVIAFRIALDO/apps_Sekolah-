import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../services/api_service.dart';
import 'package:dio/dio.dart';

class ChangePasswordController extends GetxController {
  final formKey = GlobalKey<FormState>();
  
  var currentPassword = ''.obs;
  var newPassword = ''.obs;
  var confirmPassword = ''.obs;
  var isLoading = false.obs;

  bool _obscureCurrent = true;
  bool _obscureNew = true;
  bool _obscureConfirm = true;

  bool get obscureCurrent => _obscureCurrent;
  bool get obscureNew => _obscureNew;
  bool get obscureConfirm => _obscureConfirm;

  void toggleCurrent() {
    _obscureCurrent = !_obscureCurrent;
    update();
  }

  void toggleNew() {
    _obscureNew = !_obscureNew;
    update();
  }

  void toggleConfirm() {
    _obscureConfirm = !_obscureConfirm;
    update();
  }

  Future<void> submit() async {
    if (!formKey.currentState!.validate()) return;
    
    if (newPassword.value != confirmPassword.value) {
      Get.snackbar('Error', 'Password baru dan konfirmasi tidak cocok', snackPosition: SnackPosition.BOTTOM, backgroundColor: Colors.red.shade800, colorText: Colors.white);
      return;
    }

    isLoading.value = true;
    try {
      final dio = ApiService().dio;
      final response = await dio.patch('/profile/password', data: {
        'current_password': currentPassword.value,
        'new_password': newPassword.value,
        'new_password_confirmation': confirmPassword.value,
      });

      if (response.statusCode == 200) {
        Get.back();
        Get.snackbar('Sukses', 'Password berhasil diubah!', snackPosition: SnackPosition.BOTTOM, backgroundColor: Colors.green.shade800, colorText: Colors.white);
      }
    } on DioException catch (e) {
      String message = 'Gagal mengubah password.';
      if (e.response?.statusCode == 400 || e.response?.statusCode == 422) {
        message = e.response?.data['message'] ?? message;
      }
      Get.snackbar('Error', message, snackPosition: SnackPosition.BOTTOM, backgroundColor: Colors.red.shade800, colorText: Colors.white);
    } finally {
      isLoading.value = false;
    }
  }
}
