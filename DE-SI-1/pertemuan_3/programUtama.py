import kumpulanFungsi
import Person

c = kumpulanFungsi.jumlah(56,78)
print(c)

kumpulanFungsi.mhs(nama="Juki",prodi="SI",nilai=56)
print("\nDaftar Mahasiswa")
mhs = Person.Person("098","Deni")
mhs.cetak()
mhs1 = Person.Person("099","Budi")
mhs1.cetak()
mhs2 = Person.Person("100","Bani")
mhs2.cetak()