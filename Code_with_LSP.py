#Liskov Substitution Principle
#Mahardika Yumna W. (K3525032)

from abc import ABC, abstractmethod

class Hewan(ABC):
  def __init__(self, nama, jenis):
    self.nama = nama
    self.jenis = jenis

  @abstractmethod
  def makan(self):
    pass

class HewanTerbang(Hewan):

  @abstractmethod
  def terbang(self):
    pass

class Sapi(Hewan):
  def makan(self):
    print(f"{self.nama} sedang makan rumput")

class Burung(HewanTerbang):
  def makan(self):
    print(f"{self.nama} sedang makan padi")

  def terbang(self):
    print(f"{self.nama} sedang terbang")

class Kandang:
  def __init__(self):
    self.hewan_list = []

  def tambah_hewan(self, hewan):
    self.hewan_list.append(hewan)

class KebunBinatang:
  def __init__(self):
    self.kandang = Kandang()

  def rawat_semua_hewan(self):
    for hewan in self.kandang.hewan_list:
      hewan.makan()

      if isinstance(hewan, HewanTerbang):
        hewan.terbang()

sapi = Sapi("Sepi", "Mamalia")
burung = Burung("Rakatoa", "Terbang")

zoo = KebunBinatang()

zoo.kandang.tambah_hewan(sapi)
zoo.kandang.tambah_hewan(burung)

zoo.rawat_semua_hewan()
