class KebunBinatang:
    # Menerima object kandang dari luar (Dependency Injection)
    def _init_(self, kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
