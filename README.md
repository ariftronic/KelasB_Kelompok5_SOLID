# Belajar-Github-Kelompok-5-PBO-PTIK25

Project ini dibuat untuk memenuhi tugas mata kuliah Pemrograman Berbasis Objek (PBO). Fokus utama dari project ini adalah melakukan analisis mendalam dan implementasi perbaikan kode berdasarkan 5 prinsip **SOLID** menggunakan bahasa pemrograman Python.

## 👥 Anggota Kelompok 5
1. **Mahardika Yumna Waratmaja** (K3525032) - *Liskov Substitution Principle (LSP)*
2. **Muhammad Nur Arif** (K3525034) - *Dependency Inversion Principle (DIP)*
3. **Afrizal Affandi Ahmad** (K3525046) - *Open-Closed Principle (OCP)*
4. **Awang Bintang M Lazuardi** (K3525052) - *Single Responsibility Principle (SRP)*
5. **Danang Rafli Juvianto** (K3525054) - *Interface Segregation Principle (ISP)*

---

## 📄 Deskripsi Proyek
Proyek ini menganalisis sebuah program simulasi pengelolaan Kebun Binatang yang awalnya dirancang dengan buruk (*bad code*) sehingga melanggar seluruh prinsip SOLID. Kami kemudian melakukan *refactoring* (perbaikan struktur kode) agar sistem menjadi lebih modular, mudah dirawat, dan siap untuk dikembangkan di masa depan tanpa merusak fitur yang sudah ada.

---

## ❌ Kode Awal (Melanggar Prinsip SOLID)

Berikut adalah kode pemrograman awal yang menjadi objek analisis kami:

```python
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()
```
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
## Kode Hasil Perbaikan (Memenuhi Semua Prinsip SOLID)
```python
from abc import ABC, abstractmethod

# --- INTERFACES / ABSTRACT CLASSES (ISP & OCP) ---
class Pemakan(ABC):
    @abstractmethod
    def makan(self):
        pass

class Penerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class Fasilitas(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass

    @abstractmethod
    def daftar_hewan(self):
        pass


# --- CONCRETE CLASSES (LSP & SRP) ---
class Burung(Pemakan, Penerbang):
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} mematuk biji-bijian.")

    def terbang(self):
        print(f"{self.nama} mengepakkan sayap dan terbang.")

class Kucing(Pemakan):
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} sedang makan ikan.")


# --- LOW-LEVEL MODULE (DIP) ---
class Kandang(Fasilitas):
    def __init__(self, nama_kandang):
        self.nama_kandang = nama_kandang
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def daftar_hewan(self):
        return self.hewan_list


# --- SEPARATE RESPONSIBILITY (SRP) ---
class PetugasKebersihan:
    @staticmethod
    def bersihkan_fasilitas(fasilitas_nama):
        print(f"Fasilitas {fasilitas_nama} telah selesai dibersihkan.")


# --- HIGH-LEVEL MODULE (DIP / DEPENDENCY INJECTION) ---
class KebunBinatang:
    def __init__(self, fasilitas: Fasilitas):
        self.fasilitas = fasilitas  # Bergantung pada abstraksi Fasilitas, bukan Kandang langsung

    def beri_makan_dan_aktivitas(self):
        print("--- Memulai Perawatan Hewan ---")
        for hewan in self.fasilitas.daftar_hewan():
            hewan.makan()
            
            # Pengecekan polimorfisme yang aman tanpa merusak LSP
            if isinstance(hewan, Penerbang):
                hewan.terbang()


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    kandang_utama = Kandang("Kandang Utama")
    kandang_utama.tambah_hewan(Kucing("Cemplon"))
    kandang_utama.tambah_hewan(Burung("Hantu"))

    # Dependency Injection
    sistem_kebun_binatang = KebunBinatang(kandang_utama)
    sistem_kebun_binatang.beri_makan_dan_aktivitas()

    # SRP dalam aksi
    PetugasKebersihan.bersihkan_fasilitas(kandang_utama.nama_kandang)
```

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
