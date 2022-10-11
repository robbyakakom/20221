import pymongo

klien = pymongo.MongoClient("mongodb://localhost:27017/")

dbPerpus = klien["perpustakaan"]

koleksi = dbPerpus["buku"]

buku = {"kode": "K001", "judul_buku": "Pemrograman Python", "pengarang": "Budiman", "penerbit": "Andi Offset"}

x = koleksi.insert_one(buku)

print(x.inserted_id)

