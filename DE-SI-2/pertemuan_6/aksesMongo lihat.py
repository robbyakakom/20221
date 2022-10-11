import pymongo

klien = pymongo.MongoClient("mongodb://localhost:27017/")

dbPerpus = klien["perpustakaan"]

koleksi = dbPerpus["buku"]

dataBuku = koleksi.find()

for item in dataBuku :
    print("Kode Buku ", item['kode'])
    print("Judul Buku ", item['judul_buku'])
    print("Pengarang Buku ", item['pengarang'])
    print("Penerbit Buku ", item['penerbit'])

