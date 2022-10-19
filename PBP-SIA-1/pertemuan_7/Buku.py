class Buku :
    def __init__(self, Judul, Pengarang, Penerbit, Tahun) :
        self.Judul = Judul 
        self.Pengarang = Pengarang 
        self.Penerbit = Penerbit 
        self.Tahun = Tahun 

    def tampil(self) :
        print("Judul : ",self.Judul)
        print("Pengarang : ",self.Pengarang)
        print("Penerbit : ",self.Penerbit)
        print("Tahun : ",self.Tahun)