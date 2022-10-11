import pymongo

klien = pymongo.MongoClient("mongodb://localhost:27017/")

dbtoko = klien["toko"]

koleksi = dbtoko["barang"]

# barang = {"kode": "K001", "namaBarang": "Kemeja", "jumlah": 23, "harga": 56000}

# x = koleksi.insert_one(barang)

# print(x.inserted_id)

for x in koleksi.find():
   print(x)
