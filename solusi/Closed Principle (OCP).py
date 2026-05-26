from abc import ABC, abstractmethod

class Hewan(ABC):
    def _init_(self, nama):
        self.nama = nama
    
    @abstractmethod
    def makan(self):
        pass

class Kucing(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan ikan.")
