tabelBarang = [
    {"namaBrg":"Baju","qty":20,"price":56000} ,
    {"namaBrg":"Celana","qty":35,"price":76000} ,
    {"namaBrg":"Kemeja","qty":15,"price":80000} ,
    {"namaBrg":"Kaos","qty":10,"price":45000} ,
]

print('{:-<37}'.format("-"))
print('{:11} {:<7} {:<9} {:<9} '.format("Nama Barang","Jumlah","Harga","Total"))
print('{:-<37}'.format("-"))
for rBarang in tabelBarang :
    # operasi hitung total
    rBarang["total"] = rBarang["qty"] * rBarang["price"]
    # tampilkan data
    print('{:11} {:<7} {:<9} {:<9} '.format(rBarang["namaBrg"],rBarang["qty"],rBarang["price"],rBarang["total"]))
print('{:-<37}'.format("-"))