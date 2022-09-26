barang = {"kode":"B001","namaBrg":"Baju","harga":56000,"jumlah":20}
# for dBarang in barang :
#     print(dBarang, barang[dBarang])

barang["harga"] = 75000
barang.setdefault("total", barang["harga"] * barang["jumlah"] )

# print(barang.items())
for key,val in barang.items() :
    print(key,val)