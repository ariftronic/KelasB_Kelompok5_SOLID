# Belajar-Github-Kelompok-5-PBO-PTIK25
Untuk belajar PBO 
## Analisis Prinsip SOLID pada Python

## Kelompok 5
1. Muhammad Nur Arif (K3525034)
2. Mahardika Yumna Waratmaja (K3525032)
3. Danang Rafli Juvianto (K3525054)
4. Awang Bintang M Lazuardi (K3525052)
5. Afrizal Affandi Ahmad (K3525054)

## Deskripsi
Project ini dibuat untuk menganalisis penerapan prinsip SOLID pada program Python bertema Kebun Binatang.


# Analisis Penerapan Prinsip SOLID

Berikut adalah hasil analisis tim mengenai prinsip SOLID mana saja yang sudah terpenuhi atau dilanggar pada kode awal program Kebun Binatang:

---

### 👤 Single Responsibility Principle (Awang)
> **Status:** ❌ Dilanggar

**Analisis:**
Kelas memiliki lebih dari satu tanggung jawab. Kelas `Hewan` tidak hanya menyimpan data dan perilaku umum hewan, tetapi juga memiliki method `terbang()` yang tidak dimiliki semua hewan. Lalu, kelas `KebunBinatang` juga bertanggung jawab mengatur perawatan hewan melalui method `rawat_semua_hewan()`. Jadi, tanggung jawab setiap kelas jadi tidak fokus dan kode sulit dikembangkan.

---

### 👤 Open/Closed Principle (Afrizal)
> **Status:** ❌ Dilanggar

**Analisis:**
Kode saat ini belum terbuka untuk perluasan (*open for extension*) dan tertutup untuk modifikasi (*closed for modification*). Jika ke depannya kita ingin menambahkan jenis hewan baru dengan perilaku unik (misalnya hewan yang berenang atau melompat), kita terpaksa harus memodifikasi kelas `Hewan` secara langsung atau mengubah logika di dalam method `rawat_semua_hewan()` pada kelas `KebunBinatang` dengan banyak percabangan (`if-else`).

---

### 👤 Liskov Substitution Principle (Dika)
> **Status:** ❌ Dilanggar

**Analisis:**
Pelanggaran terjadi karena pada kelas `Hewan` dipaksa agar bisa `terbang()`, kelas `KebunBinatang` memaksa semua objek hewan untuk terbang. Jika kita membuat *subclass* hewan yang tidak bisa terbang (seperti Kucing atau Gajah), *subclass* tersebut tidak dapat menggantikan peran kelas induknya (`Hewan`) dengan benar tanpa merusak logika program.

---

### 👤 Interface Segregation Principle (Danang)
> **Status:** ❌ Dilanggar

**Analisis:**
Pelanggaran ISP terdapat pada method `terbang()` di dalam kelas `Hewan`. Method tersebut membuat semua objek hewan harus memiliki kemampuan terbang, padahal tidak semua hewan dapat melakukannya. Contohnya seperti gajah, ikan, dan kucing yang sebenarnya tidak membutuhkan method tersebut. Hal ini menunjukkan bahwa *interface* pada kelas `Hewan` terlalu luas dan tidak spesifik sesuai kebutuhan masing-masing objek.

---

### 👤 Dependency Inversion Principle (Arif)
> **Status:** ❌ Dilanggar

**Analisis:**
Kelas tingkat tinggi `KebunBinatang` bergantung secara langsung pada kelas tingkat rendah `Kandang` di dalam konstruktornya (`self.kandang = Kandang()`), bukan bergantung pada abstraksi. Hal ini membuat kedua kelas tersebut terikat sangat erat (*tightly coupled*), sehingga sulit jika kita ingin mengganti atau mengembangkan jenis kandang yang berbeda di masa depan.
## Isi Repository
- 

# Solusi Perubahan Kode: Pemenuhan Prinsip SOLID

Berikut adalah langkah-langkah dan solusi perubahan kode agar sistem memenuhi kelima prinsip SOLID:

### 1. Single Responsibility Principle / SRP (Awang)
Solusinya adalah memisahkan tanggung jawab setiap class sesuai fungsinya. Class `Hewan` hanya mengatur data dan perilaku dasar hewan. Logika spesifik seperti `terbang()` dan proses `perawatan` dipindahkan ke class lain yang terpisah. Dengan begitu, setiap class hanya memiliki satu alasan untuk berubah (satu tanggung jawab) sesuai prinsip SRP.

### 2. Open-Closed Principle / OCP (Afrizal)
Solusinya adalah menggunakan abstraksi (seperti *Abstract Base Class*) pada class `Hewan`. Jika kita ingin menambahkan jenis hewan baru atau perilaku baru di masa depan, kita tidak perlu memodifikasi kode pada class utama (menghindari tumpukan kondisi `if-else`). Kita cukup membuat class turunan baru yang mengimplementasikan abstraksi tersebut. Sistem menjadi terbuka untuk perluasan (ekstensi), namun tertutup untuk modifikasi.

### 3. Liskov Substitution Principle / LSP (Dika)
Untuk menyelesaikan permasalahan yang ada, kita memisahkan antara method hewan dan class hewan umum, kemudian membuat class baru khusus hewan terbang. Dengan pendekatan ini, setiap objek dari class turunan akan selalu dapat menggantikan objek dari class induknya tanpa merusak fungsi atau ekspektasi program.

### 4. Interface Segregation Principle / ISP (Danang)
Solusi yang dilakukan adalah memisahkan method `terbang()` ke dalam class atau *interface* khusus untuk hewan yang memang dapat terbang. Hal ini mencegah hewan yang tidak bisa terbang (misalnya mamalia darat) dipaksa untuk mengimplementasikan atau bergantung pada *method* yang sama sekali tidak mereka butuhkan.

### 5. Dependency Inversion Principle / DIP (Arif)
Class `KebunBinatang` (sebagai modul tingkat tinggi) kini tidak lagi bergantung secara langsung pada class `Kandang` (modul tingkat rendah). Keduanya sekarang bergantung pada sebuah abstraksi, yaitu `IFasilitasHewan`. Implementasinya dilakukan melalui metode *Dependency Injection* di dalam `__init__`.

## Prinsip yang Dianalisis
- Single Responsibility Principle
- Open Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle
