#data tabel Barang
tabelBarang = [
    {"kode":"K001","nmBrg":"Kemeja","price":50000,"qty":30},
    {"kode":"B001","nmBrg":"Baju","price":57000,"qty":20},
    {"kode":"C001","nmBrg":"Celana","price":65000,"qty":50},
    {"kode":"K002","nmBrg":"Kaos","price":40000,"qty":5},
]

print("---------------------------------------------------------------")
print('{:6} {:15} {:9} {:9} {:9} {:9}'.format("Kode","NamaBarang","Harga","Qty","Total","Diskon")) 
print("---------------------------------------------------------------")
for iBarang in tabelBarang :
    #dioperasikan
    iBarang["total"] = iBarang["price"] * iBarang["qty"]
    if iBarang['qty'] > 25 :
        iBarang["diskon"] = 0.25 * iBarang["total"]
    else :
        iBarang["diskon"] = 0

    print('{:6} {:15} {:<9} {:<9} {:<9} {:<9}'.format(iBarang['kode'],iBarang['nmBrg'],iBarang['price'],iBarang['qty'],iBarang['total'],iBarang['diskon'])) 
print("---------------------------------------------------------------")