# Dependency Inversion Principle (DIP)

Dependency Inversion Principle adalah salah satu prinsip dalam SOLID yang menyatakan bahwa *class* tingkat tinggi (*high-level modules*) tidak boleh bergantung secara langsung pada *class* tingkat rendah (*low-level modules*). Keduanya seharusnya bergantung pada sebuah abstraksi (*interface* atau *abstract class*). Prinsip ini bertujuan agar komponen-komponen di dalam sistem tidak saling terikat kuat (*tightly coupled*), sehingga desain program menjadi lebih rapi, fleksibel, dan mudah dikembangkan.

Secara sederhana, DIP mengajarkan bahwa kode kita sebaiknya berinteraksi dengan "kerangka" atau standar umum, bukan langsung memanggil objek yang spesifik. Jika sebuah *class* utama langsung membuat dan menggunakan objek dari *class* lain di dalamnya (*hardcoded*), maka hal tersebut termasuk pelanggaran DIP. Dengan menerapkan DIP (misalnya melalui teknik *Dependency Injection*), program akan lebih mudah dipelihara dan komponennya bisa dibongkar-pasang tanpa merusak sistem inti.

# Ciri-Ciri Pelanggaran DIP

Pelanggaran Dependency Inversion Principle biasanya terjadi ketika sebuah *class* utama (*high-level*) menginisialisasi atau memanggil detail *class* bawahan (*low-level*) secara langsung di dalam kodenya. Hal ini menyebabkan kedua *class* tersebut menjadi sangat bergantung satu sama lain. Akibatnya, desain program menjadi kaku; ketika kita ingin menambahkan fitur baru atau mengubah cara kerja *class* bawahan, kita terpaksa harus ikut membongkar dan memodifikasi kode pada *class* utama yang sebenarnya sudah berjalan dengan baik.

# Tujuan DIP

Tujuan dari Dependency Inversion Principle adalah untuk memisahkan ketergantungan langsung antar komponen di dalam program. Dengan menggunakan abstraksi sebagai jembatan, program menjadi lebih modular, lebih mudah dites, dan lebih fleksibel ketika ingin dikembangkan. DIP memastikan bahwa perubahan pada detail teknis di modul tingkat rendah tidak akan mengganggu atau merusak logika alur kerja di modul tingkat tinggi.

---

## Analisis Pada Kode Program

Pada kode program awal, pelanggaran DIP terdapat pada method `__init__` di dalam class `PaymentProcessor`.

```python
class PaymentProcessor:
    def __init__(self):
        self.payment_method = CreditCardPayment()
```
Baris kode tersebut membuat class PaymentProcessor (modul tingkat tinggi) bergantung secara langsung pada pembuatan objek dari class CreditCardPayment (modul tingkat rendah).

Sistem ini menjadi sangat kaku (tightly coupled). Jika sewaktu-waktu kita ingin menambahkan metode pembayaran baru (misalnya QRIS atau transfer bank), kita terpaksa harus membongkar dan memodifikasi isi dari class PaymentProcessor ini secara langsung. Oleh karena itu, kode program ini melanggar prinsip Dependency Inversion Principle (DIP) karena tidak bergantung pada sebuah abstraksi.

Solusi DIP
Solusi yang dapat dilakukan adalah membuat sebuah abstraksi atau interface (misalnya class PaymentMethod) sebagai kerangka standar untuk semua metode pembayaran. Kemudian, kita mengubah class PaymentProcessor agar menerima abstraksi tersebut melalui parameternya (menggunakan teknik Dependency Injection), bukan lagi menciptakan objek pembayarannya sendiri di dalam method.

Contoh perbaikannya:
```python
from abc import ABC, abstractmethod

# 1. Membuat Abstraksi
class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

# 2. Modul Tingkat Rendah bergantung pada abstraksi
class CreditCardPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Paid {amount} using Credit Card.")

# 3. Modul Tingkat Tinggi bergantung pada abstraksi
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method
        
    def pay(self, amount):
        self.payment_method.make_payment(amount)
```

Dengan perbaikan tersebut, class PaymentProcessor tidak lagi peduli dengan detail spesifik dari jenis pembayarannya. Kita kini bebas menambahkan jenis class pembayaran baru dengan sangat mudah tanpa perlu merusak class inti, sehingga program menjadi jauh lebih dinamis dan sesuai dengan prinsip Dependency Inversion Principle.

