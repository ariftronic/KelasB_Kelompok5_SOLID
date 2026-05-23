class Hewan:
  def __init__(self, nama, jenis):
    self.nama = nama
    self.jenis = jenis

  def makan(self):
    print(f"Hewan {self.nama} sedang makan.")

class HewanTerbang(Hewan):
  def terbang(self):
    print(f"Hewan {self.nama} bisa terbang.")

class Burung(HewanTerbang):
  pass

class Sapi(Hewan):
  pass 

class Kandang:
  def __init__(self):
    self.hewan_list = []

  def tambah_hewan(self, hewan):
    self.hewan_list.append(hewan)

  def bersihkan_kandang(self):
    print("Kandang dibersihkan")

class KebunBinatang:
  def __init__(self):
    self.kandang = Kandang()

  def rawat_semua_hewan(self):
    for hewan in self.kandang.hewan_list:
      hewan.makan()
      
      if isinstance(hewan, HewanTerbang):
            hewan.terbang()

burung = Burung("Perkutut", "Burung")
sapi = Sapi("sapi", "mamalia")

zoo = KebunBinatang()

zoo.kandang.tambah_hewan(burung)
zoo.kandang.tambah_hewan(sapi)

zoo.rawat_semua_hewan()
