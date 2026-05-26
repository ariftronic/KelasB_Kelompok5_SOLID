## Dependency Inversion Principle (DIP)
Dependency Inversion Principle (DIP) pada dasarnya memiliki dua aturan utama yang wajib dipegang:

1. High-level modules should not depend on low-level modules. Both should depend on abstractions. (Modul tingkat tinggi tidak boleh bergantung pada modul tingkat rendah. Keduanya harus sama-sama bergantung pada abstraksi).

2. Abstractions should not depend on details. Details should depend on abstractions. (Abstraksi tidak boleh bergantung pada detail implementasi. Justru detail itulah yang harus bergantung pada abstraksi).

Dalam struktur kode, class tingkat tinggi (yang biasanya berisi core logic atau aturan bisnis utama) tidak boleh berinteraksi langsung dengan class tingkat rendah (yang mengurus hal teknis/detail). Keduanya harus dijembatani oleh sebuah "kerangka" standar, seperti Interface atau Abstract Class.

Pembalikan (inversion) arah ketergantungan ini dilakukan supaya sistem tidak saling mengikat terlalu kuat (tight coupling).

## Ciri-Ciri Kode yang Melanggar DIP
Kapan kode kita disebut melanggar DIP? Paling gampang dilihat kalau ada sebuah class utama (high-level) yang langsung melakukan inisialisasi atau pembuatan objek dari class lain (low-level) di dalam konstruktor atau method-nya (biasanya hardcoded).

Praktik seperti ini bikin dua class tersebut jadi sangat bergantung satu sama lain. Efek buruknya, desain program jadi kaku. Pas kita butuh nambah fitur baru atau sekadar ngubah cara kerja class bawahan, kita terpaksa harus bongkar-bongkar lagi kode di class utama yang sebenarnya sudah jalan normal.

## Tujuan Utama DIP
Inti dari penerapan DIP adalah memutus rantai ketergantungan langsung antar komponen tersebut biar jadi loosely coupled (terikat lemah).

Dengan menjadikan abstraksi sebagai jembatan (biasanya dibantu dengan teknik Dependency Injection), kode kita bakal jadi lebih modular, gampang dites (testable), dan fleksibel. Kita bebas membongkar-pasang atau menambah detail teknis di modul tingkat rendah tanpa takut merusak atau mengganggu alur kerja di modul tingkat tinggi.
