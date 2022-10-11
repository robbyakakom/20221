import pymongo

klien = pymongo.MongoClient("mongodb://localhost:27017/")

dbtoko = klien["toko"]

print(dbtoko)
