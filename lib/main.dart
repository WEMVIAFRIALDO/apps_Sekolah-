import 'package:flutter/material.dart';

void main() {
  runApp(const AplikasiSekolah());
}

class AplikasiSekolah extends StatelessWidget {
  const AplikasiSekolah({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false, // Menghilangkan pita merah 'Debug' di layar
      title: 'Aplikasi Sekolah',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const BerandaSekolah(),
    );
  }
}

class BerandaSekolah extends StatelessWidget {
  const BerandaSekolah({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Beranda Sekolah'),
        backgroundColor: Colors.blue,
        foregroundColor: Colors.white,
      ),
      body: const Center(
        child: Text(
          'Selamat datang di Aplikasi Sekolah Wemvi!',
          style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
        ),
      ),
    );
  }
}