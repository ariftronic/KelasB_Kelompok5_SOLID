# Single Responsibility Principle
# Awang Bintang M Lazuardi (K3525052)

from abc import ABC, abstractmethod

class IFasilitasHewan(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass

    @abstractmethod
    def get_hewan(self):
        pass

class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

class HewanTerbang(Hewan):
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Burung(HewanTerbang):
    pass
class Kucing(Hewan):
    pass
class Gajah(Hewan):
    pass

class Kandang(IFasilitasHewan):
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def get_hewan(self):
        return self.hewan_list

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class PerawatHewan:
    def rawat(self, hewan):
        hewan.makan()

        if isinstance(hewan, HewanTerbang):
            hewan.terbang()

class KebunBinatang:
    def __init__(self, fasilitas_hewan):
        self.kandang = fasilitas_hewan
        self.perawat = PerawatHewan()

    def rawat_semua_hewan(self):
        for hewan in self.kandang.get_hewan():
            self.perawat.rawat(hewan)

kandang = Kandang()
burung = Burung("Elang", "Burung")
kucing = Kucing("Milo", "Mamalia")
gajah = Gajah("Dumbo", "Mamalia")

kandang.tambah_hewan(burung)
kandang.tambah_hewan(kucing)
kandang.tambah_hewan(gajah)

kandang.bersihkan_kandang()
print()

kebun_binatang = KebunBinatang(kandang)
kebun_binatang.rawat_semua_hewan()
