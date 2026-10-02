import 'package:flutter_test/flutter_test.dart';
import 'package:apps_sekolah/main.dart';

void main() {
  testWidgets('SALUT App smoke test', (WidgetTester tester) async {
    // Build SALUT app dan trigger frame pertama
    await tester.pumpWidget(const SalutApp());

    // Verifikasi login page muncul (ada teks 'SALUT')
    expect(find.text('SALUT'), findsOneWidget);
  });
}
