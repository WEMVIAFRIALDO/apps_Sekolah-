import 'package:get/get.dart';
import '../services/api_service.dart';

class SkillsController extends GetxController {
  final _api = ApiService();

  var isLoading = false.obs;
  var errorMessage = ''.obs;
  var userJurusan = ''.obs;

  // Daftar kompetensi keahlian
  var allSkills = <Map<String, dynamic>>[].obs;
  var filteredSkills = <Map<String, dynamic>>[].obs;
  var selectedFilter = 'Semua'.obs;

  @override
  void onInit() {
    super.onInit();
    fetchMySkills();
  }

  Future<void> fetchMySkills() async {
    try {
      isLoading.value = true;
      errorMessage.value = '';

      final response = await _api.get('/skills/my');
      final data = response.data;

      if (data['success'] == true) {
        userJurusan.value = data['jurusan']?.toString() ?? 'SMK';
        final list = (data['data'] as List? ?? [])
            .map((item) => Map<String, dynamic>.from(item as Map))
            .toList();

        allSkills.assignAll(list);
        applyFilter(selectedFilter.value);
      } else {
        errorMessage.value = data['message'] ?? 'Gagal memuat kompetensi.';
      }
    } catch (e) {
      errorMessage.value = ApiService.parseError(e);
    } finally {
      isLoading.value = false;
    }
  }

  void applyFilter(String filter) {
    selectedFilter.value = filter;
    if (filter == 'Semua') {
      filteredSkills.assignAll(allSkills);
    } else {
      filteredSkills.assignAll(
        allSkills.where((s) => s['level'] == filter).toList(),
      );
    }
  }

  int countByLevel(String level) {
    return allSkills.where((s) => s['level'] == level).length;
  }
}
