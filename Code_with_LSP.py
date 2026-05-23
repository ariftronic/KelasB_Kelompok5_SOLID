class Hewan(self):
  def __init__(self, nama, jenis):
    self.nama = nama
    self.jenis = jenis

  def makan(self):
    print(f"Hewan {self.nama} sedang makan.")

class HewawTerbang(Hewan):
  def __init__(self):
    print(f"Hewan {self.nama} bisa terbang.")

class Burung(HewanTerbang):
  pass

class Gajah(Hewan):
  pass 

class Kandang:
  def __init__(self):
    self.hewan_list = []

  def tambah_hewan(self):
    self.hewan_list.append(hewan)

  def bersihkan_kandang(self):
    print("Kandang dibersihkan")

class KebunBinatang(self):
  def __init__(self):
    self.kandang = kandang()

  def rawat_semua_hewan(self):
    for hewan in self.kandang.hewan_list:
      hewan.makan()

        if isistance(hewan, hewan_terbang):
          hewan.terbang()

burung = Burung(perkutut, burung)
sapi = Sapi(sapi, mamalia)

zoo = KebunBinatang()

zoo.kandang.append(burung)
zoo.kandang.append(sapi)

zoo.rawat_semua_hewan()
