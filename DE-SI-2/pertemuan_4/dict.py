barang = {"namaBrg":"Baju", "jumlah":10, "harga":45000}
barang.setdefault("kode","K0004")
barang["namaBrg"] = "Kemeja"
barang["total"] = barang["jumlah"] * barang["harga"]

for keyBarang in barang :
    print('{:10} {:<5}'.format(keyBarang, barang[keyBarang]))