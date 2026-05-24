from abc import ABC, abstractmethod

class FasilitasHewan(ABC):
    @abstractmethod
    def dapatkan_semua_hewan(self):
        pass

class Kandang(FasilitasHewan):
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
        
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

    def dapatkan_semua_hewan(self):
        return self.hewan_list

class Akuarium(FasilitasHewan):
    def __init__(self):
        self.ikan_list = []
        
    def tambah_hewan(self, ikan):
        self.ikan_list.append(ikan)
        
    def dapatkan_semua_hewan(self):
        return self.ikan_list

class KebunBinatang:
    def __init__(self, fasilitas: FasilitasHewan):
        self.fasilitas = fasilitas 

    def rawat_semua_hewan(self):
        for hewan in self.fasilitas.dapatkan_semua_hewan():
            hewan.makan()
