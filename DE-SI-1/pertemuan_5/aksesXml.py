from xml.dom.minidom import parse
penjualan = parse('barang.xml') 
jum = len(penjualan.getElementsByTagName("barang"))
i = 0 
print('{:<10} {:<12} {:<10}'.format("Kode","Nama Barang","Harga"))
while(i < jum) :
    kode = penjualan.getElementsByTagName("kode")[i].firstChild.nodeValue 
    nama = penjualan.getElementsByTagName("nama")[i].firstChild.nodeValue 
    harga = penjualan.getElementsByTagName("harga")[i].firstChild.nodeValue 
    print('{:<10} {:<12} {:<10}'.format(kode,nama,harga))
    i = i + 1