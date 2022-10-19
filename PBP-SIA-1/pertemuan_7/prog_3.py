from Buku import Buku

#instantiasi
judul = input("Judul BUku ")
pengarang = input("Pengarang BUku ")
penerbit = input("Penerbit Buku ")
tahun = input("Tahun Terbit Buku ")

buku1 = Buku(judul,pengarang,penerbit,tahun)
buku1.tampil()

# buku1.Judul = "Pemrograman Framework"
# buku1.tampil()

# buku2 = Buku("Algoritma Pemrograman","Hana Ningrum","Ando Offset","2022")
# buku2.tampil()