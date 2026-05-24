## Dependency Inversion Principle (DIP)
Berdasarkan konsep SOLID dari Robert C. Martin dan merujuk pada penjelasan di blog Rosihan Ari, prinsip Dependency Inversion Principle (DIP) memiliki dua aturan utama:

Modul tingkat tinggi (high-level modules) tidak boleh bergantung pada modul tingkat rendah (low-level modules). Keduanya harus bergantung pada abstraksi.

Abstraksi tidak boleh bergantung pada detail. Sebaliknya, detail implementasi yang harus bergantung pada abstraksi.

Singkatnya, antarkomponen di dalam kode sebaiknya berinteraksi melalui sebuah "kerangka" (seperti Interface atau Abstract Class), bukan memanggil dan membuat objek spesifik secara langsung (hardcoded). Pembalikan (inversion) ini bertujuan memutus ikatan yang kaku (tight coupling).

## Ciri-Ciri Pelanggaran DIP
Pelanggaran sering terjadi ketika sebuah class utama langsung melakukan inisialisasi class bawahan di dalam konstruktornya. Akibatnya desain menjadi kaku. Jika sewaktu-waktu kita ingin mengubah cara kerja class bawahan atau menambah fitur baru, kita terpaksa harus ikut membongkar kode pada class utama.

Tujuan utama penerapan DIP adalah memisahkan ketergantungan tersebut sehingga sistem menjadi loosely coupled (terikat lemah), lebih modular, dan adaptif terhadap perubahan tanpa harus merusak struktur program yang sudah ada.

## Analisis Kasus: Sistem Kebun Binatang
Pada struktur kode awal di bawah ini, pelanggaran DIP terlihat jelas pada method __init__ di dalam class KebunBinatang.

```python
class KebunBinatang:
    def __init__(self):
        # Pelanggaran DIP: Inisialisasi objek secara langsung (Hardcoded)
        self.kandang = Kandang()
```
Baris kode tersebut membuat class KebunBinatang bergantung secara mutlak pada detail implementasi dari class Kandang.
Merujuk pada konsep yang dijelaskan oleh Rosihan Ari, sistem ini sangat kaku. Bayangkan jika pihak kebun binatang ingin menambah fasilitas baru, misalnya Akuarium untuk ikan atau Sangkar untuk burung. Karena sudah di-hardcode, kita terpaksa harus membongkar ulang class KebunBinatang agar bisa menggunakan fasilitas baru tersebut. Ini adalah pelanggaran DIP murni karena class tingkat tinggi bergantung pada detail, bukan pada abstraksi.

## Solusi dan Refactoring Kode
Untuk menyelesaikan masalah tight coupling ini, kita perlu membalik ketergantungannya (Dependency Inversion). Solusi yang diimplementasikan:

Membuat sebuah abstraksi (Interface) sebagai standar kontrak untuk semua tempat penampungan hewan.

Memastikan class Kandang (atau class fasilitas lainnya nanti) mengimplementasikan abstraksi tersebut.

Mengubah class KebunBinatang agar menerima abstraksi dari luar (menggunakan teknik Dependency Injection pada parameternya), sehingga tidak perlu lagi menciptakan objek Kandang secara manual.

## Kode Setelah Perbaikan:
```python
from abc import ABC, abstractmethod

class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")


# 1. Membuat Abstraksi (Interface)
class IFasilitasHewan(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass

    @abstractmethod
    def dapatkan_semua_hewan(self):
        pass


# 2. Modul Tingkat Rendah mengimplementasikan abstraksi
class Kandang(IFasilitasHewan):
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
        
    def dapatkan_semua_hewan(self):
        return self.hewan_list

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")


# 3. Modul Tingkat Tinggi bergantung pada abstraksi (Dependency Injection)
class KebunBinatang:
    # Menerima abstraksi IFasilitasHewan, bukan class Kandang secara spesifik
    def __init__(self, fasilitas: IFasilitasHewan):
        self.fasilitas = fasilitas

    def rawat_semua_hewan(self):
        # Berinteraksi dengan method yang sudah distandarkan oleh Interface
        for hewan in self.fasilitas.dapatkan_semua_hewan():
            hewan.makan()
            hewan.terbang()
```

## Kesimpulan
Dengan perubahan di atas, class KebunBinatang tidak perlu lagi tahu apakah fasilitas yang digunakan berupa Kandang, Akuarium, atau TamanSafari, selama class fasilitas tersebut mengikuti kerangka dari interface IFasilitasHewan. Kita sekarang bisa dengan mudah melakukan scaling atau menambah fasilitas hewan baru tanpa perlu membongkar core logic dari class KebunBinatang.
