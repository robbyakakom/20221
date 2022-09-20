class Person :
  
  def __init__(self,nama,usia):
    self.nama = nama
    self.usia = usia

  def tampil(self):
    print("Nama ",self.nama,"Usia ",self.usia)


class Mahasiswa (Person) : # class Mahasiswa extends Person
  
  def __init__(self, nama, usia, prodi):
    super().__init__(nama, usia) 
    self.prodi = prodi

  def tampil(self):
    print("Nama ",self.nama,"Usia ",self.usia, "Prodi ", self.prodi)

objMhs = Mahasiswa("Budi","20","SI")
objMhs.tampil()

obj1 = Person("Budi",67)
obj2 = Person("Cici",88)

obj1.tampil()
obj2.tampil()