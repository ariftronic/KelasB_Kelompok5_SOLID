<div align="center">

# 🦁 Zoo Management System
### Analisis & Implementasi Prinsip SOLID dalam Python

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigma-OOP-8A2BE2?style=for-the-badge)
![SOLID](https://img.shields.io/badge/SOLID-5%2F5%20Prinsip-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Kelompok](https://img.shields.io/badge/Kelompok-5-orange?style=for-the-badge)

<br>

> 🎓 **Mata Kuliah:** Pemrograman Berbasis Objek (PBO) — PTIK 2025
>
> 🎯 **Tujuan:** Menganalisis pelanggaran prinsip SOLID pada kode awal bertema
> simulasi kebun binatang, lalu melakukan *refactoring* menyeluruh hingga
> sistem menjadi modular, mudah dirawat, dan siap dikembangkan lebih jauh.

</div>

---

## 📑 Daftar Isi

- [👥 Anggota Kelompok](#-anggota-kelompok)
- [📖 Tentang Proyek](#-tentang-proyek)
- [💡 Apa itu Prinsip SOLID?](#-apa-itu-prinsip-solid)
- [❌ Kode Awal — Melanggar Semua Prinsip SOLID](#-kode-awal--melanggar-semua-prinsip-solid)
- [🔍 Analisis Pelanggaran Per Prinsip](#-analisis-pelanggaran-per-prinsip)
- [✅ Kode Hasil Perbaikan](#-kode-hasil-perbaikan--memenuhi-semua-prinsip-solid)
- [🏗️ Arsitektur Sistem — Sebelum vs Sesudah](#️-arsitektur-sistem--sebelum-vs-sesudah)
- [🛠️ Solusi Perubahan Per Prinsip](#️-solusi-perubahan-per-prinsip)
- [📊 Tabel Perbandingan Menyeluruh](#-tabel-perbandingan-menyeluruh)
- [🚀 Cara Menjalankan](#-cara-menjalankan)
- [📤 Contoh Output Program](#-contoh-output-program)
- [📚 Referensi](#-referensi)

---

## 👥 Anggota Kelompok

<div align="center">

| No | 👤 Nama | 🪪 NIM | 📌 Prinsip | Keterangan |
|:--:|---------|--------|:----------:|------------|
| 1 | **Mahardika Yumna Waratmaja** | K3525032 | `LSP` | Liskov Substitution Principle |
| 2 | **Muhammad Nur Arif** | K3525034 | `DIP` | Dependency Inversion Principle |
| 3 | **Afrizal Affandi Ahmad** | K3525046 | `OCP` | Open-Closed Principle |
| 4 | **Awang Bintang M Lazuardi** | K3525052 | `SRP` | Single Responsibility Principle |
| 5 | **Danang Rafli Juvianto** | K3525054 | `ISP` | Interface Segregation Principle |

</div>

---

## 📖 Tentang Proyek

Proyek ini berfokus pada **analisis mendalam** dan **implementasi perbaikan kode** berdasarkan 5 prinsip desain *Object-Oriented Programming* yang dikenal dengan akronim **SOLID**.

Sebagai studi kasus, kami menggunakan program simulasi **pengelolaan Kebun Binatang** yang secara sengaja dibuat dengan struktur yang buruk (*bad code*) sehingga melanggar kelima prinsip SOLID secara bersamaan. Proses ini meliputi:

```
[1] Identifikasi       Menemukan setiap pelanggaran SOLID pada kode awal
       ↓
[2] Analisis           Memahami dampak dan konsekuensi dari setiap pelanggaran
       ↓
[3] Perencanaan        Merancang solusi refactoring yang tepat per prinsip
       ↓
[4] Implementasi       Menulis ulang kode dengan struktur yang benar
       ↓
[5] Verifikasi         Memastikan semua prinsip SOLID telah terpenuhi
```

---

## 💡 Apa itu Prinsip SOLID?

**SOLID** adalah akronim dari 5 prinsip desain perangkat lunak berorientasi objek yang diperkenalkan oleh **Robert C. Martin** (dikenal sebagai *Uncle Bob*) dan dipopulerkan oleh **Michael Feathers**. Tujuan utamanya adalah menciptakan kode yang:

- ✅ Mudah dipahami (*readable*)
- ✅ Mudah dikembangkan (*extensible*)
- ✅ Mudah diuji (*testable*)
- ✅ Mudah dirawat (*maintainable*)
- ✅ Tidak rentan terhadap perubahan kecil (*robust*)

```
╔══════════════════════════════════════════════════════════════════════╗
║                     PRINSIP S.O.L.I.D                               ║
╠══╦══════════════════════════════╦══════════════════════════════════╗ ║
║  ║ S — Single Responsibility   ║ Satu class, satu tanggung jawab  ║ ║
║  ╠══════════════════════════════╬══════════════════════════════════╣ ║
║  ║ O — Open-Closed             ║ Terbuka ekstensi, tutup modif.   ║ ║
║  ╠══════════════════════════════╬══════════════════════════════════╣ ║
║  ║ L — Liskov Substitution     ║ Subclass = pengganti superclass  ║ ║
║  ╠══════════════════════════════╬══════════════════════════════════╣ ║
║  ║ I — Interface Segregation   ║ Interface spesifik > satu umum   ║ ║
║  ╠══════════════════════════════╬══════════════════════════════════╣ ║
║  ║ D — Dependency Inversion    ║ Bergantung abstraksi, bukan impl ║ ║
║  ╚══════════════════════════════╩══════════════════════════════════╝ ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## ❌ Kode Awal — Melanggar Semua Prinsip SOLID

> ⚠️ **Perhatian:** Kode di bawah ini adalah contoh **kode yang buruk** (*bad code*) dan secara sengaja dibuat untuk keperluan analisis. Jangan dijadikan referensi implementasi.

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

    def bersihkan_kandang(self):              # ❌ Tanggung jawab tidak relevan
        print("Kandang dibersihkan.")


class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()              # ❌ Bergantung langsung pada Kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()                   # ❌ Paksa semua hewan terbang!
```

### 🗺️ Peta Masalah Kode Awal

```
KebunBinatang ──(hard-coded)──► Kandang ──► [ Hewan, Hewan, ... ]
      │                                            │
      └── rawat_semua_hewan()                      ├── makan()   ← semua OK
                │                                  └── terbang() ← MASALAH!
                └── paksa SEMUA hewan terbang()
                    (bahkan gajah, ikan, kucing...)
```

### 📋 Ringkasan Pelanggaran

| Prinsip | Status | Pelanggaran Utama |
|---------|:------:|-------------------|
| SRP | ❌ | `Kandang` punya `bersihkan_kandang()` yang bukan urusannya |
| OCP | ❌ | Tambah hewan baru → harus modifikasi kelas yang sudah ada |
| LSP | ❌ | Semua hewan dipaksa punya `terbang()` walau tidak relevan |
| ISP | ❌ | Interface `Hewan` terlalu lebar, memuat method yang tidak semua butuhkan |
| DIP | ❌ | `KebunBinatang` hard-coded bergantung pada `Kandang` secara langsung |

---

## 🔍 Analisis Pelanggaran Per Prinsip

---

### 🔴 Prinsip 1 — Single Responsibility Principle (SRP)
#### *Dikerjakan oleh: Awang Bintang M Lazuardi (K3525052)*

> *"A class should have only one reason to change."*
> — Robert C. Martin

**Status: ❌ Dilanggar**

**Deskripsi Masalah:**

Dalam kode awal, terdapat percampuran tanggung jawab yang seharusnya dipisahkan:

| Kelas | Tanggung Jawab yang Dicampur | Seharusnya |
|-------|------------------------------|------------|
| `Hewan` | Menyimpan data + mendefinisikan perilaku terbang | Hanya data & perilaku umum |
| `Kandang` | Menyimpan hewan + membersihkan kandang | Hanya menyimpan hewan |
| `KebunBinatang` | Mengelola sistem + merawat hewan langsung | Hanya mengkoordinasikan |

**Dampak Nyata:**
- Perubahan kecil pada logika kebersihan memaksa kita menyentuh kelas `Kandang`
- Perubahan proses perawatan memaksa kita menyentuh kelas `KebunBinatang`
- Setiap kelas memiliki lebih dari satu alasan untuk berubah — melanggar SRP

---

### 🔴 Prinsip 2 — Open-Closed Principle (OCP)
#### *Dikerjakan oleh: Afrizal Affandi Ahmad (K3525046)*

> *"Software entities should be open for extension, but closed for modification."*
> — Bertrand Meyer

**Status: ❌ Dilanggar**

**Deskripsi Masalah:**

Kode awal tidak menggunakan abstraksi sama sekali. Akibatnya, setiap kali ingin menambahkan jenis hewan baru, kita **wajib memodifikasi** kode yang sudah ada:

```python
# Gambaran kondisi yang akan terjadi jika dikembangkan tanpa OCP:
def rawat_semua_hewan(self):
    for hewan in self.kandang.hewan_list:
        hewan.makan()
        if hewan.jenis == "burung":
            hewan.terbang()         # if-else menumpuk seiring waktu
        elif hewan.jenis == "ikan":
            hewan.berenang()        # terus bertambah...
        elif hewan.jenis == "katak":
            hewan.melompat()        # ...dan bertambah lagi
        elif hewan.jenis == "harimau":
            hewan.mengaum()         # tidak ada habisnya!
```

**Dampak Nyata:**
- Setiap penambahan hewan baru = modifikasi kode lama yang sudah berjalan
- Risiko bug meningkat setiap kali ada perubahan
- Kode menjadi panjang, penuh `if-else`, dan sulit dibaca

---

### 🔴 Prinsip 3 — Liskov Substitution Principle (LSP)
#### *Dikerjakan oleh: Mahardika Yumna Waratmaja (K3525032)*

> *"Objects of a subclass should be replaceable with objects of the superclass
> without altering the correctness of the program."*
> — Barbara Liskov

**Status: ❌ Dilanggar**

**Deskripsi Masalah:**

Kelas `KebunBinatang` memanggil `terbang()` pada **semua** objek `Hewan` tanpa pengecualian. Hal ini menyebabkan pelanggaran LSP ketika membuat subclass:

```python
# Contoh pelanggaran LSP yang akan terjadi:

class Kucing(Hewan):
    def terbang(self):
        raise Exception("Kucing tidak bisa terbang! 🐱")   # ❌ Program crash!

class Gajah(Hewan):
    def terbang(self):
        raise NotImplementedError("Gajah tidak bisa terbang! 🐘")  # ❌ LSP dilanggar

# Kode ini akan merusak program saat dijalankan:
kebun = KebunBinatang()
kebun.kandang.tambah_hewan(Kucing("Cemplon"))
kebun.rawat_semua_hewan()  # 💥 CRASH! Kucing dipaksa terbang
```

**Dampak Nyata:**
- Subclass tidak dapat menggantikan superclass-nya dengan aman
- Program crash saat runtime jika ada hewan yang tidak bisa terbang
- Pewarisan menjadi tidak dapat diandalkan

---

### 🔴 Prinsip 4 — Interface Segregation Principle (ISP)
#### *Dikerjakan oleh: Danang Rafli Juvianto (K3525054)*

> *"Clients should not be forced to depend on interfaces they do not use."*
> — Robert C. Martin

**Status: ❌ Dilanggar**

**Deskripsi Masalah:**

Semua hewan dipaksa memiliki method `terbang()`, meski sebagian besar hewan di dunia nyata tidak bisa terbang. Ini adalah interface yang terlalu lebar dan tidak spesifik:

| 🐾 Hewan | Perlu `makan()` | Perlu `terbang()` | Kondisi Nyata |
|---------|:--------------:|:-----------------:|---------------|
| 🦅 Elang | ✅ | ✅ | Bisa terbang |
| 🦆 Bebek | ✅ | ✅ | Bisa terbang |
| 🐱 Kucing | ✅ | ❌ | Tidak bisa terbang |
| 🐟 Ikan | ✅ | ❌ | Tidak bisa terbang |
| 🐘 Gajah | ✅ | ❌ | Tidak bisa terbang |
| 🐍 Ular | ✅ | ❌ | Tidak bisa terbang |

**Dampak Nyata:**
- 4 dari 6 hewan di atas dipaksa bergantung pada method yang tidak mereka butuhkan
- Interface kelas `Hewan` "gemuk" dan tidak mencerminkan dunia nyata
- Perubahan pada `terbang()` mempengaruhi semua hewan, bahkan yang tidak terbang

---

### 🔴 Prinsip 5 — Dependency Inversion Principle (DIP)
#### *Dikerjakan oleh: Muhammad Nur Arif (K3525034)*

> *"High-level modules should not depend on low-level modules. Both should
> depend on abstractions. Abstractions should not depend on details.
> Details should depend on abstractions."*
> — Robert C. Martin

**Status: ❌ Dilanggar**

**Deskripsi Masalah:**

`KebunBinatang` (modul tingkat tinggi) secara eksplisit membuat dan bergantung pada `Kandang` (modul tingkat rendah):

```python
class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()   # ❌ Hard-coded! Tightly coupled!
```

```
Kondisi Sekarang (SALAH):         Kondisi Ideal (BENAR):

KebunBinatang                     KebunBinatang
      │                                 │
      │ bergantung langsung             │ bergantung pada abstraksi
      ▼                                 ▼
   Kandang                          «interface»
                                     Fasilitas
                                         ▲
                                         │ implementasi
                                      Kandang
```

**Dampak Nyata:**
- Mengganti `Kandang` dengan `KandangLuar` atau `AquariumBesar` memaksa perubahan di `KebunBinatang`
- Pengujian unit (*unit testing*) menjadi sulit karena tidak bisa di-*mock*
- Kedua modul terikat erat dan tidak bisa dikembangkan secara independen

---

## ✅ Kode Hasil Perbaikan — Memenuhi Semua Prinsip SOLID

```python
from abc import ABC, abstractmethod


# ╔══════════════════════════════════════════════════════════════════════╗
# ║          LAYER 1: INTERFACES / ABSTRACT BASE CLASSES                ║
# ║          Memenuhi: ISP (interface spesifik) & OCP (abstraksi)        ║
# ╚══════════════════════════════════════════════════════════════════════╝

class Pemakan(ABC):
    """
    Interface untuk SEMUA hewan yang memiliki kemampuan makan.
    Setiap hewan di kebun binatang pasti butuh makan.
    """
    @abstractmethod
    def makan(self):
        pass


class Penerbang(ABC):
    """
    Interface KHUSUS untuk hewan yang memiliki kemampuan terbang.
    Tidak semua hewan implement interface ini — hanya yang bisa terbang.
    Memenuhi ISP: interface spesifik sesuai kebutuhan.
    """
    @abstractmethod
    def terbang(self):
        pass


class Fasilitas(ABC):
    """
    Abstraksi untuk berbagai jenis fasilitas penampung hewan.
    Bisa berupa Kandang biasa, Aquarium, Kandang Luar, dsb.
    Memenuhi DIP: KebunBinatang bergantung pada abstraksi ini, bukan implementasi konkret.
    """
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass

    @abstractmethod
    def daftar_hewan(self):
        pass


# ╔══════════════════════════════════════════════════════════════════════╗
# ║          LAYER 2: CONCRETE ANIMAL CLASSES                           ║
# ║          Memenuhi: SRP (tanggung jawab tunggal) & LSP (aman diganti) ║
# ╚══════════════════════════════════════════════════════════════════════╝

class Burung(Pemakan, Penerbang):
    """
    Burung bisa MAKAN dan TERBANG.
    Implement kedua interface sesuai kemampuan nyata burung.
    Memenuhi LSP: dapat menggantikan Pemakan atau Penerbang tanpa masalah.
    """
    def __init__(self, nama: str):
        self.nama = nama

    def makan(self):
        print(f"🐦 {self.nama} mematuk biji-bijian.")

    def terbang(self):
        print(f"🐦 {self.nama} mengepakkan sayap dan terbang tinggi.")


class Kucing(Pemakan):
    """
    Kucing HANYA bisa makan — tidak implement Penerbang.
    Tidak dipaksa terbang. Memenuhi ISP dan LSP.
    """
    def __init__(self, nama: str):
        self.nama = nama

    def makan(self):
        print(f"🐱 {self.nama} lahap memakan ikan kesukaannya.")


class Ikan(Pemakan):
    """
    Contoh ekstensi di masa depan — TANPA mengubah kode lama sama sekali.
    Cukup buat class baru yang implement interface yang sesuai.
    Memenuhi OCP: sistem terbuka untuk ekstensi.
    """
    def __init__(self, nama: str):
        self.nama = nama

    def makan(self):
        print(f"🐟 {self.nama} memakan plankton di permukaan air.")


# ╔══════════════════════════════════════════════════════════════════════╗
# ║          LAYER 3: LOW-LEVEL MODULE                                  ║
# ║          Memenuhi: DIP (implementasi dari abstraksi Fasilitas)       ║
# ╚══════════════════════════════════════════════════════════════════════╝

class Kandang(Fasilitas):
    """
    Implementasi konkret dari abstraksi Fasilitas.
    KebunBinatang tidak perlu tahu bahwa ini adalah Kandang secara spesifik.
    """
    def __init__(self, nama_kandang: str):
        self.nama_kandang = nama_kandang
        self._hewan_list = []

    def tambah_hewan(self, hewan: Pemakan):
        self._hewan_list.append(hewan)
        print(f"✔ {hewan.nama} berhasil ditambahkan ke {self.nama_kandang}.")

    def daftar_hewan(self):
        return self._hewan_list


# ╔══════════════════════════════════════════════════════════════════════╗
# ║          LAYER 4: SEPARATED RESPONSIBILITY                          ║
# ║          Memenuhi: SRP (kebersihan = tanggung jawab sendiri)         ║
# ╚══════════════════════════════════════════════════════════════════════╝

class PetugasKebersihan:
    """
    Satu-satunya tanggung jawab class ini: menangani kebersihan fasilitas.
    Dipisah dari Kandang dan KebunBinatang sesuai prinsip SRP.
    """
    @staticmethod
    def bersihkan_fasilitas(fasilitas: Fasilitas):
        if isinstance(fasilitas, Kandang):
            print(f"🧹 Fasilitas '{fasilitas.nama_kandang}' telah dibersihkan.")
        else:
            print("🧹 Fasilitas telah dibersihkan.")


# ╔══════════════════════════════════════════════════════════════════════╗
# ║          LAYER 5: HIGH-LEVEL MODULE                                 ║
# ║          Memenuhi: DIP (via Dependency Injection di constructor)     ║
# ╚══════════════════════════════════════════════════════════════════════╝

class KebunBinatang:
    """
    Modul tingkat tinggi yang mengkoordinasikan seluruh sistem.
    Bergantung pada abstraksi 'Fasilitas', bukan implementasi konkret 'Kandang'.
    Fasilitas disuntikkan dari luar (Dependency Injection).
    """
    def __init__(self, fasilitas: Fasilitas):
        self.fasilitas = fasilitas

    def beri_makan_dan_aktivitas(self):
        print("\n" + "═" * 45)
        print("   🦁  MEMULAI SESI PERAWATAN HEWAN  🦁")
        print("═" * 45)

        for hewan in self.fasilitas.daftar_hewan():
            hewan.makan()

            # isinstance() adalah pengecekan polimorfisme yang aman ✅
            # Tidak melanggar LSP karena hanya hewan yang BENAR-BENAR
            # implement Penerbang yang akan dipanggil terbang()
            if isinstance(hewan, Penerbang):
                hewan.terbang()

            print()

        print("═" * 45)
        print("   ✅  Sesi perawatan selesai.")
        print("═" * 45 + "\n")


# ╔══════════════════════════════════════════════════════════════════════╗
# ║                        MAIN EXECUTION                               ║
# ╚══════════════════════════════════════════════════════════════════════╝

if __name__ == "__main__":

    print("\n🏗️  Menyiapkan kandang dan mengisi hewan...\n")

    # Setup fasilitas
    kandang_utama = Kandang("Kandang Utama")

    # Tambahkan hewan ke kandang
    kandang_utama.tambah_hewan(Kucing("Cemplon"))
    kandang_utama.tambah_hewan(Burung("Hantu"))
    kandang_utama.tambah_hewan(Ikan("Nemo"))

    # Dependency Injection — KebunBinatang tidak tahu soal Kandang secara spesifik
    sistem = KebunBinatang(kandang_utama)

    # Jalankan sesi perawatan
    sistem.beri_makan_dan_aktivitas()

    # SRP dalam aksi — kebersihan ditangani oleh class yang tepat
    petugas = PetugasKebersihan()
    petugas.bersihkan_fasilitas(kandang_utama)
```

---

## 🏗️ Arsitektur Sistem — Sebelum vs Sesudah

### ❌ Sebelum Refactoring

```
┌─────────────────────────────────┐
│          KebunBinatang          │
│  ┌───────────────────────────┐  │
│  │ self.kandang = Kandang()  │  │  ← Hard-coded dependency
│  └───────────────────────────┘  │
│  rawat_semua_hewan()            │
│    ├── hewan.makan()            │
│    └── hewan.terbang() ⚠️       │  ← Paksa semua terbang
└────────────┬────────────────────┘
             │
             ▼
    ┌─────────────────┐
    │     Kandang     │
    │  hewan_list[]   │
    │  bersihkan() ⚠️  │  ← Tanggung jawab tidak sesuai
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │     Hewan       │
    │  makan()        │
    │  terbang() ⚠️   │  ← Tidak semua hewan bisa terbang!
    └─────────────────┘
```

### ✅ Sesudah Refactoring

```
         ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
         │  «abstract»  │    │  «abstract»  │    │  «abstract»  │
         │   Pemakan    │    │  Penerbang   │    │  Fasilitas   │
         │  + makan()   │    │  + terbang() │    │+tambah_hewan │
         └──────┬───────┘    └──────┬───────┘    │+daftar_hewan │
                │                   │            └──────┬───────┘
       ┌────────┼────────┐          │                   │
       ▼        ▼        ▼          │                   ▼
   ┌───────┐ ┌──────┐ ┌──────┐     │           ┌──────────────┐
   │Kucing │ │Burung│ │ Ikan │◄────┘           │    Kandang   │
   │makan()│ │makan │ │makan │                 │tambah_hewan()│
   └───────┘ │terbng│ └──────┘                 │daftar_hewan()│
             └──────┘                          └──────┬───────┘
                                                      │ injeksi
                                              ┌───────▼────────┐
                                              │  KebunBinatang │
                                              │ fasilitas:     │
                                              │  Fasilitas     │
                                              │ beri_makan_    │
                                              │  _aktivitas()  │
                                              └────────────────┘

         ┌────────────────────┐
         │ PetugasKebersihan  │  ← Tanggung jawab kebersihan dipisah (SRP)
         │ bersihkan_         │
         │   fasilitas()      │
         └────────────────────┘
```

---

## 🛠️ Solusi Perubahan Per Prinsip

---

### ✅ Solusi SRP — Single Responsibility Principle *(Awang)*

**Strategi:** Pisahkan setiap class sesuai satu tanggung jawab yang jelas.

| Class | Tanggung Jawab Tunggal |
|-------|------------------------|
| `Burung`, `Kucing`, `Ikan` | Mendefinisikan perilaku hewan masing-masing |
| `Kandang` | Menyimpan dan mengelola daftar hewan |
| `PetugasKebersihan` | Menangani kebersihan fasilitas |
| `KebunBinatang` | Mengkoordinasikan perawatan hewan secara keseluruhan |

> 💡 **Kunci SRP:** Tanyakan — *"Apa satu-satunya alasan class ini perlu berubah?"* Jika ada lebih dari satu jawaban, class tersebut melanggar SRP.

---

### ✅ Solusi OCP — Open-Closed Principle *(Afrizal)*

**Strategi:** Gunakan *Abstract Base Class* sehingga ekstensi cukup dengan membuat class baru.

```python
# Ingin tambah Elang? Cukup buat class baru — tanpa sentuh kode lama:
class Elang(Pemakan, Penerbang):
    def __init__(self, nama): self.nama = nama
    def makan(self): print(f"🦅 {self.nama} menyambar mangsa.")
    def terbang(self): print(f"🦅 {self.nama} melayang di ketinggian.")

# Ingin tambah Buaya? Sama, cukup class baru:
class Buaya(Pemakan):
    def __init__(self, nama): self.nama = nama
    def makan(self): print(f"🐊 {self.nama} menerkam mangsa di tepi sungai.")

# KebunBinatang, Kandang, dan class lain TIDAK perlu diubah sama sekali! ✅
```

---

### ✅ Solusi LSP — Liskov Substitution Principle *(Dika)*

**Strategi:** Pisahkan interface berdasarkan kemampuan aktual, bukan asumsi.

```python
# ✅ BENAR: Kucing hanya implement Pemakan — tidak ada terbang() palsu
class Kucing(Pemakan):
    def makan(self): ...     # ✅ Aman digunakan sebagai Pemakan

# ✅ BENAR: Burung implement keduanya sesuai kemampuan nyata
class Burung(Pemakan, Penerbang):
    def makan(self): ...     # ✅ Aman sebagai Pemakan
    def terbang(self): ...   # ✅ Aman sebagai Penerbang

# Substitusi yang aman:
pemakan: Pemakan = Kucing("Cemplon")   # ✅ Berfungsi sempurna
pemakan: Pemakan = Burung("Hantu")    # ✅ Berfungsi sempurna
penerbang: Penerbang = Burung("Hantu") # ✅ Berfungsi sempurna
```

---

### ✅ Solusi ISP — Interface Segregation Principle *(Danang)*

**Strategi:** Pecah interface besar menjadi interface-interface kecil yang spesifik.

```
Interface SEBELUM (❌ terlalu lebar):       Interface SESUDAH (✅ spesifik):

┌────────────────┐                         ┌────────────────┐
│    Hewan       │                         │    Pemakan     │
│────────────────│                         │────────────────│
│ + makan()      │                         │ + makan()      │
│ + terbang()    │                         └────────────────┘
└────────────────┘                         ┌────────────────┐
   ↑ dipaksa ke                            │   Penerbang    │
   SEMUA hewan                             │────────────────│
                                           │ + terbang()    │
                                           └────────────────┘
                                              ↑ hanya untuk
                                              hewan yg terbang
```

---

### ✅ Solusi DIP — Dependency Inversion Principle *(Arif)*

**Strategi:** Gunakan Dependency Injection dan bergantung pada abstraksi.

```python
# ❌ SEBELUM: Hard-coded, tidak bisa diganti
class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()   # Terikat erat ke Kandang

# ✅ SESUDAH: Fleksibel via Dependency Injection
class KebunBinatang:
    def __init__(self, fasilitas: Fasilitas):
        self.fasilitas = fasilitas  # Bergantung pada abstraksi

# Sekarang bisa digunakan dengan fasilitas apapun:
kebun1 = KebunBinatang(Kandang("Kandang A"))
kebun2 = KebunBinatang(Aquarium("Aquarium Laut"))       # implementasi baru
kebun3 = KebunBinatang(KandangLuar("Area Savana"))      # implementasi baru
# KebunBinatang tidak perlu dimodifikasi sama sekali! ✅
```

---

## 📊 Tabel Perbandingan Menyeluruh

<div align="center">

| Aspek | ❌ Sebelum Refactoring | ✅ Sesudah Refactoring |
|:------|:----------------------|:----------------------|
| **Jumlah Class** | 3 class | 7 class (lebih terstruktur) |
| **Abstract Base Class** | Tidak ada | 3 ABC (`Pemakan`, `Penerbang`, `Fasilitas`) |
| **Coupling** | Tightly coupled | Loosely coupled |
| **Ekstensi Hewan Baru** | Harus modifikasi kode lama | Cukup buat class baru |
| **Tanggung Jawab** | Bercampur dalam satu class | Terpisah jelas |
| **Penanganan Terbang** | Paksa semua hewan terbang | Hanya yang implement `Penerbang` |
| **Dependency** | Hard-coded `Kandang` | Injeksi via abstraksi `Fasilitas` |
| **Unit Testing** | Sangat sulit (tightly coupled) | Mudah (bisa di-mock) |
| **Risiko Bug** | Tinggi saat perubahan kecil | Rendah, perubahan terisolasi |
| **Keterbacaan Kode** | 🔴 Rendah | 🟢 Tinggi |
| **Skalabilitas** | 🔴 Terbatas | 🟢 Sangat baik |
| **Reusability** | 🔴 Tidak ada | 🟢 Setiap class bisa dipakai ulang |

</div>

---

## 🚀 Cara Menjalankan

### Prasyarat

- Python **3.10** atau lebih baru
- Tidak ada dependensi eksternal

### Langkah-langkah

```bash
# 1. Clone repository ini
git clone https://github.com/username/Belajar-Github-Kelompok-5-PBO-PTIK25.git

# 2. Masuk ke direktori proyek
cd Belajar-Github-Kelompok-5-PBO-PTIK25

# 3. (Opsional) Jalankan kode AWAL yang melanggar SOLID
python zoo_bad.py

# 4. Jalankan kode hasil PERBAIKAN yang memenuhi SOLID
python zoo_solid.py
```

### Struktur File

```
Belajar-Github-Kelompok-5-PBO-PTIK25/
│
├── 📄 README.md              ← Dokumentasi proyek (file ini)
├── 🐍 zoo_bad.py             ← Kode awal yang melanggar SOLID
├── 🐍 zoo_solid.py           ← Kode hasil refactoring (SOLID)
└── 📁 docs/
    ├── analisis_srp.md       ← Analisis mendalam SRP (Awang)
    ├── analisis_ocp.md       ← Analisis mendalam OCP (Afrizal)
    ├── analisis_lsp.md       ← Analisis mendalam LSP (Dika)
    ├── analisis_isp.md       ← Analisis mendalam ISP (Danang)
    └── analisis_dip.md       ← Analisis mendalam DIP (Arif)
```

---

## 📤 Contoh Output Program

```
🏗️  Menyiapkan kandang dan mengisi hewan...

✔ Cemplon berhasil ditambahkan ke Kandang Utama.
✔ Hantu berhasil ditambahkan ke Kandang Utama.
✔ Nemo berhasil ditambahkan ke Kandang Utama.

═════════════════════════════════════════════
   🦁  MEMULAI SESI PERAWATAN HEWAN  🦁
═════════════════════════════════════════════
🐱 Cemplon lahap memakan ikan kesukaannya.

🐦 Hantu mematuk biji-bijian.
🐦 Hantu mengepakkan sayap dan terbang tinggi.

🐟 Nemo memakan plankton di permukaan air.

═════════════════════════════════════════════
   ✅  Sesi perawatan selesai.
═════════════════════════════════════════════

🧹 Fasilitas 'Kandang Utama' telah dibersihkan.
```

---

## 📚 Referensi

- 📖 Martin, R.C. (2003). *Agile Software Development: Principles, Patterns, and Practices*. Prentice Hall.
- 📖 Martin, R.C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
- 🌐 [SOLID Principles — Real Python](https://realpython.com/solid-principles-python/)
- 🌐 [Python ABC Documentation](https://docs.python.org/3/library/abc.html)
- 🌐 [Refactoring.Guru — SOLID](https://refactoring.guru/design-principles/solid)

---

<div align="center">

**— Kelompok 5, PBO PTIK 2025 —**

*"Any fool can write code that a computer can understand.*
*Good programmers write code that humans can understand."*

— Martin Fowler

<br>

![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SOLID](https://img.shields.io/badge/Follows-SOLID%20Principles-brightgreen?style=flat-square)
![Love](https://img.shields.io/badge/Made%20with-❤️-red?style=flat-square)

</div>
