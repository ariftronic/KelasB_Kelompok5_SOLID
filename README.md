# 🦁 Simulasi Kebun Binatang
## Analisis & Refactoring Prinsip SOLID

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Prinsip](https://img.shields.io/badge/SOLID-5%2F5%20Prinsip-orange?style=for-the-badge)
![Kelompok](https://img.shields.io/badge/Kelompok-5-blue?style=for-the-badge)

> 📚 **Mata Kuliah:** Pemrograman Berbasis Objek (PBO) — PTIK 2025
> 🎯 **Tujuan:** Menganalisis pelanggaran prinsip SOLID pada kode awal, lalu melakukan *refactoring* menyeluruh agar sistem menjadi modular, mudah dirawat, dan siap dikembangkan.

---

## 📑 Daftar Isi

- [👥 Anggota Kelompok](#-anggota-kelompok)
- [📖 Tentang Proyek](#-tentang-proyek)
- [💡 Apa itu SOLID?](#-apa-itu-solid)
- [❌ Kode Awal](#-kode-awal-melanggar-semua-prinsip-solid)
- [🔍 Analisis Pelanggaran](#-analisis-pelanggaran-solid)
- [✅ Kode Hasil Perbaikan](#-kode-hasil-perbaikan-memenuhi-semua-prinsip-solid)
- [🛠️ Solusi per Prinsip](#️-solusi-perubahan-per-prinsip)
- [📊 Perbandingan Sebelum & Sesudah](#-perbandingan-sebelum--sesudah)
- [🚀 Cara Menjalankan](#-cara-menjalankan)

---

## 👥 Anggota Kelompok

<table>
  <thead>
    <tr>
      <th>No</th>
      <th>Nama</th>
      <th>NIM</th>
      <th>Prinsip</th>
      <th>Keterangan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>🧑‍💻 Mahardika Yumna Waratmaja</td>
      <td>K3525032</td>
      <td><b>LSP</b></td>
      <td>Liskov Substitution Principle</td>
    </tr>
    <tr>
      <td>2</td>
      <td>🧑‍💻 Muhammad Nur Arif</td>
      <td>K3525034</td>
      <td><b>DIP</b></td>
      <td>Dependency Inversion Principle</td>
    </tr>
    <tr>
      <td>3</td>
      <td>🧑‍💻 Afrizal Affandi Ahmad</td>
      <td>K3525046</td>
      <td><b>OCP</b></td>
      <td>Open-Closed Principle</td>
    </tr>
    <tr>
      <td>4</td>
      <td>🧑‍💻 Awang Bintang M Lazuardi</td>
      <td>K3525052</td>
      <td><b>SRP</b></td>
      <td>Single Responsibility Principle</td>
    </tr>
    <tr>
      <td>5</td>
      <td>🧑‍💻 Danang Rafli Juvianto</td>
      <td>K3525054</td>
      <td><b>ISP</b></td>
      <td>Interface Segregation Principle</td>
    </tr>
  </tbody>
</table>

---

## 📖 Tentang Proyek

Proyek ini menganalisis program simulasi pengelolaan **Kebun Binatang** yang awalnya dirancang dengan buruk (*bad code*) sehingga melanggar seluruh prinsip **SOLID**. Kami kemudian melakukan *refactoring* menyeluruh agar sistem menjadi:

| Sebelum Refactoring | Sesudah Refactoring |
|---|---|
| 🔴 Kode sulit dirawat | 🟢 Modular & mudah dirawat |
| 🔴 Tightly coupled | 🟢 Loosely coupled |
| 🔴 Sulit dikembangkan | 🟢 Siap dikembangkan |
| 🔴 Melanggar 5 prinsip SOLID | 🟢 Memenuhi 5 prinsip SOLID |
| 🔴 Tidak ada abstraksi | 🟢 Menggunakan Abstract Base Class |

---

## 💡 Apa itu SOLID?

**SOLID** adalah akronim dari 5 prinsip desain perangkat lunak berorientasi objek yang dikemukakan oleh **Robert C. Martin** (*Uncle Bob*). Tujuannya adalah membuat kode lebih mudah dipahami, dirawat, dan dikembangkan.

```
S  →  Single Responsibility Principle  →  Satu class, satu tanggung jawab
O  →  Open-Closed Principle            →  Terbuka untuk ekstensi, tertutup untuk modifikasi
L  →  Liskov Substitution Principle    →  Subclass harus bisa menggantikan superclass-nya
I  →  Interface Segregation Principle  →  Interface spesifik lebih baik dari satu interface umum
D  →  Dependency Inversion Principle   →  Bergantung pada abstraksi, bukan implementasi konkret
```

---

## ❌ Kode Awal (Melanggar Semua Prinsip SOLID)

> ⚠️ Kode di bawah ini adalah **contoh kode yang buruk** dan sengaja dibuat untuk dianalisis.

```python
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):                        # ❌ Tidak semua hewan bisa terbang!
        print(f"{self.nama} sedang terbang.")

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self):              # ❌ Tanggung jawab tidak relevan di sini
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()              # ❌ Bergantung langsung pada Kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()                   # ❌ Paksa semua hewan terbang!
```

### 🧩 Struktur Kode Awal

```
KebunBinatang
    └── Kandang (hard-coded, tightly coupled)
            └── Hewan (makan + terbang — semua digabung)
```

---

## 🔍 Analisis Pelanggaran SOLID

---

### 🔴 1. Single Responsibility Principle — SRP *(Awang Bintang M Lazuardi)*

> *"A class should have only one reason to change."*

**Status:** ❌ **Dilanggar**

**Masalah:**
- Kelas `Hewan` merangkap sebagai penyimpan data **sekaligus** mendefinisikan perilaku `terbang()` yang tidak dimiliki semua hewan
- Kelas `KebunBinatang` ikut bertanggung jawab atas proses perawatan melalui `rawat_semua_hewan()`
- Kelas `Kandang` memiliki method `bersihkan_kandang()` yang seharusnya menjadi tanggung jawab entitas lain

**Dampak:** Jika logika perawatan berubah, kita harus menyentuh kelas `KebunBinatang`. Jika logika kebersihan berubah, kita harus menyentuh kelas `Kandang`. Satu perubahan kecil bisa merusak banyak bagian.

---

### 🔴 2. Open-Closed Principle — OCP *(Afrizal Affandi Ahmad)*

> *"Software entities should be open for extension, but closed for modification."*

**Status:** ❌ **Dilanggar**

**Masalah:**
- Menambah hewan baru dengan perilaku unik (berenang, melompat) **mengharuskan modifikasi** kelas `Hewan` yang sudah ada
- Metode `rawat_semua_hewan()` akan dipenuhi percabangan `if-else` seiring bertambahnya jenis hewan

**Gambaran masalah:**
```python
# Yang akan terjadi jika terus mengembangkan kode lama:
def rawat_semua_hewan(self):
    for hewan in self.kandang.hewan_list:
        hewan.makan()
        if hewan.jenis == "burung":
            hewan.terbang()       # ❌ if-else menumpuk
        elif hewan.jenis == "ikan":
            hewan.berenang()
        elif hewan.jenis == "katak":
            hewan.melompat()
        # ... dan seterusnya
```

---

### 🔴 3. Liskov Substitution Principle — LSP *(Mahardika Yumna Waratmaja)*

> *"Objects of a subclass should be replaceable with objects of the superclass without breaking the application."*

**Status:** ❌ **Dilanggar**

**Masalah:**
- `KebunBinatang` memanggil `terbang()` pada **semua** objek `Hewan` tanpa terkecuali
- Jika dibuat subclass `Kucing(Hewan)` atau `Gajah(Hewan)`, kedua subclass ini tidak bisa menggantikan `Hewan` dengan benar karena mereka tidak bisa terbang

**Gambaran masalah:**
```python
class Kucing(Hewan):
    def terbang(self):
        raise Exception("Kucing tidak bisa terbang!")  # ❌ Melanggar LSP
```

---

### 🔴 4. Interface Segregation Principle — ISP *(Danang Rafli Juvianto)*

> *"Clients should not be forced to depend on interfaces they do not use."*

**Status:** ❌ **Dilanggar**

**Masalah:**
- Semua objek `Hewan` dipaksa memiliki method `terbang()`, meski sebagian besar hewan tidak membutuhkannya
- Hewan seperti **gajah**, **ikan**, dan **kucing** terpaksa "mewarisi" kemampuan terbang yang tidak relevan

| Hewan | Perlu `makan()` | Perlu `terbang()` |
|-------|:-:|:-:|
| 🦅 Burung | ✅ | ✅ |
| 🐱 Kucing | ✅ | ❌ |
| 🐘 Gajah | ✅ | ❌ |
| 🐟 Ikan | ✅ | ❌ |

---

### 🔴 5. Dependency Inversion Principle — DIP *(Muhammad Nur Arif)*

> *"High-level modules should not depend on low-level modules. Both should depend on abstractions."*

**Status:** ❌ **Dilanggar**

**Masalah:**
- `KebunBinatang` (modul tingkat tinggi) secara langsung membuat instance `Kandang` (modul tingkat rendah) di dalam konstruktornya
- Keduanya *tightly coupled* — mengganti `Kandang` dengan jenis fasilitas lain mengharuskan modifikasi kelas `KebunBinatang`

```python
class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()   # ❌ Hard-coded dependency
```

---

## ✅ Kode Hasil Perbaikan (Memenuhi Semua Prinsip SOLID)

```python
from abc import ABC, abstractmethod

# ╔══════════════════════════════════════════════════════════════╗
# ║        INTERFACES / ABSTRACT CLASSES  (ISP & OCP)           ║
# ╚══════════════════════════════════════════════════════════════╝

class Pemakan(ABC):
    """Interface untuk semua hewan yang bisa makan."""
    @abstractmethod
    def makan(self):
        pass

class Penerbang(ABC):
    """Interface khusus untuk hewan yang bisa terbang."""
    @abstractmethod
    def terbang(self):
        pass

class Fasilitas(ABC):
    """Abstraksi untuk berbagai jenis fasilitas kandang."""
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass

    @abstractmethod
    def daftar_hewan(self):
        pass


# ╔══════════════════════════════════════════════════════════════╗
# ║           CONCRETE CLASSES  (SRP & LSP)                     ║
# ╚══════════════════════════════════════════════════════════════╝

class Burung(Pemakan, Penerbang):
    """Burung bisa makan DAN terbang."""
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} mematuk biji-bijian.")

    def terbang(self):
        print(f"{self.nama} mengepakkan sayap dan terbang.")

class Kucing(Pemakan):
    """Kucing hanya bisa makan — tidak perlu implement terbang."""
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} sedang makan ikan.")


# ╔══════════════════════════════════════════════════════════════╗
# ║             LOW-LEVEL MODULE  (DIP)                         ║
# ╚══════════════════════════════════════════════════════════════╝

class Kandang(Fasilitas):
    """Implementasi konkret dari abstraksi Fasilitas."""
    def __init__(self, nama_kandang):
        self.nama_kandang = nama_kandang
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def daftar_hewan(self):
        return self.hewan_list


# ╔══════════════════════════════════════════════════════════════╗
# ║           SEPARATE RESPONSIBILITY  (SRP)                    ║
# ╚══════════════════════════════════════════════════════════════╝

class PetugasKebersihan:
    """Satu-satunya tanggung jawab: membersihkan fasilitas."""
    @staticmethod
    def bersihkan_fasilitas(fasilitas_nama):
        print(f"Fasilitas '{fasilitas_nama}' telah selesai dibersihkan.")


# ╔══════════════════════════════════════════════════════════════╗
# ║      HIGH-LEVEL MODULE  (DIP — Dependency Injection)        ║
# ╚══════════════════════════════════════════════════════════════╝

class KebunBinatang:
    """Bergantung pada abstraksi Fasilitas, bukan Kandang secara langsung."""
    def __init__(self, fasilitas: Fasilitas):
        self.fasilitas = fasilitas

    def beri_makan_dan_aktivitas(self):
        print("\n🦁 ===== Memulai Perawatan Hewan ===== 🦁")
        for hewan in self.fasilitas.daftar_hewan():
            hewan.makan()
            if isinstance(hewan, Penerbang):   # Polimorfisme aman ✅
                hewan.terbang()
        print("✅ Perawatan selesai.\n")


# ╔══════════════════════════════════════════════════════════════╗
# ║                    MAIN EXECUTION                           ║
# ╚══════════════════════════════════════════════════════════════╝

if __name__ == "__main__":
    # Setup kandang dan isi dengan hewan
    kandang_utama = Kandang("Kandang Utama")
    kandang_utama.tambah_hewan(Kucing("Cemplon"))
    kandang_utama.tambah_hewan(Burung("Hantu"))

    # Dependency Injection — KebunBinatang tidak perlu tahu soal Kandang secara spesifik
    sistem_kebun_binatang = KebunBinatang(kandang_utama)
    sistem_kebun_binatang.beri_makan_dan_aktivitas()

    # SRP dalam aksi — kebersihan ditangani oleh class yang tepat
    PetugasKebersihan.bersihkan_fasilitas(kandang_utama.nama_kandang)
```

### 🧩 Struktur Kode Setelah Refactoring

```
Abstraksi
├── Pemakan (ABC)           ← semua hewan implement ini
├── Penerbang (ABC)         ← hanya hewan terbang
└── Fasilitas (ABC)         ← semua jenis kandang

Implementasi
├── Burung (Pemakan, Penerbang)
├── Kucing (Pemakan)
└── Kandang (Fasilitas)

Tanggung Jawab Terpisah
├── PetugasKebersihan       ← urusan kebersihan
└── KebunBinatang(Fasilitas)← urusan perawatan hewan (via DI)
```

---

## 🛠️ Solusi Perubahan per Prinsip

### ✅ 1. SRP — Single Responsibility Principle *(Awang)*

Memisahkan tanggung jawab setiap class sesuai fungsinya:
- `Burung` / `Kucing` → hanya mengatur perilaku hewan masing-masing
- `PetugasKebersihan` → hanya mengurus kebersihan fasilitas
- `KebunBinatang` → hanya mengkoordinasikan perawatan

> **Kunci:** Setiap class hanya punya **satu alasan untuk berubah**.

---

### ✅ 2. OCP — Open-Closed Principle *(Afrizal)*

Menggunakan *Abstract Base Class* sehingga menambah jenis hewan baru cukup dengan membuat **class turunan baru** tanpa menyentuh kode yang sudah ada.

```python
# Contoh ekstensi di masa depan — tanpa ubah kode lama sama sekali:
class Ikan(Pemakan):
    def makan(self):
        print(f"{self.nama} memakan plankton.")

class Elang(Pemakan, Penerbang):
    def makan(self): ...
    def terbang(self): ...
```

---

### ✅ 3. LSP — Liskov Substitution Principle *(Dika)*

Memisahkan interface `Pemakan` dan `Penerbang`. Setiap subclass kini dapat **menggantikan superclass-nya** tanpa merusak logika program karena tidak ada pemaksaan kemampuan yang tidak dimiliki.

---

### ✅ 4. ISP — Interface Segregation Principle *(Danang)*

Method `terbang()` dipindahkan ke interface `Penerbang` yang terpisah. Hasilnya:

| Hewan | Implement `Pemakan` | Implement `Penerbang` |
|-------|:-:|:-:|
| 🦅 Burung | ✅ | ✅ |
| 🐱 Kucing | ✅ | ➖ (tidak dipaksa) |
| 🐟 Ikan | ✅ | ➖ (tidak dipaksa) |

---

### ✅ 5. DIP — Dependency Inversion Principle *(Arif)*

`KebunBinatang` kini bergantung pada abstraksi `Fasilitas`, bukan langsung ke `Kandang`. Ketergantungan disuntikkan melalui *Dependency Injection* di konstruktor.

```python
# Fleksibel! Bisa diganti dengan fasilitas apapun di masa depan:
kandang_vip = KandangVIP("Zona Premium")
kebun = KebunBinatang(kandang_vip)   # ✅ Tidak perlu ubah KebunBinatang
```

---

## 📊 Perbandingan Sebelum & Sesudah

| Aspek | ❌ Sebelum | ✅ Sesudah |
|---|---|---|
| **Jumlah Class** | 3 class | 7 class (lebih terstruktur) |
| **Abstraksi** | Tidak ada | 3 Abstract Base Class |
| **Coupling** | Tightly coupled | Loosely coupled |
| **Kemampuan Ekstensi** | Harus modifikasi kode lama | Cukup tambah class baru |
| **Tanggung Jawab** | Bercampur dalam 1 class | Terpisah jelas per class |
| **Penanganan Polimorfisme** | Paksa semua hewan terbang | Cek dengan `isinstance()` |
| **Dependency** | Hard-coded `Kandang` | Injeksi via abstraksi |
| **Maintainability** | 🔴 Rendah | 🟢 Tinggi |

---

## 🚀 Cara Menjalankan

**Prasyarat:** Python 3.10 atau lebih baru

```bash
# Clone repository
git clone https://github.com/username/Belajar-Github-Kelompok-5-PBO-PTIK25.git

# Masuk ke direktori proyek
cd Belajar-Github-Kelompok-5-PBO-PTIK25

# Jalankan kode hasil perbaikan
python solid_refactored.py
```

**Output yang diharapkan:**
```
🦁 ===== Memulai Perawatan Hewan ===== 🦁
Cemplon sedang makan ikan.
Hantu mematuk biji-bijian.
Hantu mengepakkan sayap dan terbang.
✅ Perawatan selesai.

Fasilitas 'Kandang Utama' telah selesai dibersihkan.
```

---

<div align="center">

**Kelompok 5 — PBO PTIK 2025**

*"Clean code is not written by following a set of rules. Clean code is written by a programmer who cares."*
— Robert C. Martin

</div>
