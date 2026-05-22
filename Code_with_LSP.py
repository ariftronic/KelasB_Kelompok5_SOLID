class Hewan(self):
  def __init__(self, nama, jenis):
    self.nama = nama
    self.jenis = jenis

  def makan(self):
    print(f"Hewan {self.nama} sedang makan.")

class HewawTerbang(Hewan):
  def __init__(self):
    print(f"Hewan {self.nama} bisa terbang.")

#BELUM SELESAI!
