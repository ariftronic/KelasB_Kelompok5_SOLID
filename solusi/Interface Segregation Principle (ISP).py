class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self): pass

class Burung(Hewan, BisaTerbang):
    def makan(self):
        print(f"{self.nama} makan biji-bijian.")
    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")
