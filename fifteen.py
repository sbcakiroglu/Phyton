#inheritance

class Insan:
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim
        
    def selamla(self):
        print(f"Merhabalar efendim benim adım... {self.isim}")
    
    def yemek_rica_et(self):
        print("Rica etsem bana döner verebilir misiniz?")
        
    def ismini_soyle(self):
        print(f"Benim adım {self.name} ve soyadım {self.soyisim}")
       
    def maasini_soyle(self):
        print("Söylenmez ayıp")
        
class KibarInsan():
    pass

kibar_insan = KibarInsan("Hasan", "Tatar")
kibar_insan.maasini_soyle()
