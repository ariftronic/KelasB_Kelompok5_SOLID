# Dependency Inversion Principle (DIP)

Dependency Inversion Principle adalah salah satu prinsip dalam SOLID yang menyatakan bahwa *class* tingkat tinggi (*high-level modules*) tidak boleh bergantung secara langsung pada *class* tingkat rendah (*low-level modules*). Keduanya seharusnya bergantung pada sebuah abstraksi (*interface* atau *abstract class*). Prinsip ini bertujuan agar komponen-komponen di dalam sistem tidak saling terikat kuat (*tightly coupled*), sehingga desain program menjadi lebih rapi, fleksibel, dan mudah dikembangkan.

Secara sederhana, DIP mengajarkan bahwa kode kita sebaiknya berinteraksi dengan "kerangka" atau standar umum, bukan langsung memanggil objek yang spesifik. Jika sebuah *class* utama langsung membuat dan menggunakan objek dari *class* lain di dalamnya (*hardcoded*), maka hal tersebut termasuk pelanggaran DIP. Dengan menerapkan DIP (misalnya melalui teknik *Dependency Injection*), program akan lebih mudah dipelihara dan komponennya bisa dibongkar-pasang tanpa merusak sistem inti.

## Ciri-Ciri Pelanggaran DIP

Pelanggaran Dependency Inversion Principle biasanya terjadi ketika sebuah *class* utama (*high-level*) menginisialisasi atau memanggil detail *class* bawahan (*low-level*) secara langsung di dalam kodenya. Hal ini menyebabkan kedua *class* tersebut menjadi sangat bergantung satu sama lain. Akibatnya, desain program menjadi kaku; ketika kita ingin menambahkan fitur baru atau mengubah cara kerja *class* bawahan, kita terpaksa harus ikut membongkar dan memodifikasi kode pada *class* utama yang sebenarnya sudah berjalan dengan baik.

## Tujuan DIP

Tujuan dari Dependency Inversion Principle adalah untuk memisahkan ketergantungan langsung antar komponen di dalam program. Dengan menggunakan abstraksi sebagai jembatan, program menjadi lebih modular, lebih mudah dites, dan lebih fleksibel ketika ingin dikembangkan. DIP memastikan bahwa perubahan pada detail teknis di modul tingkat rendah tidak akan mengganggu atau merusak logika alur kerja di modul tingkat tinggi.
