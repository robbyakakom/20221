def kali(x,y) :
    return (x * y)

def mahasiswa(nim,nama,prodi="SI") :
    print(nim, nama, prodi)

def nama(*data) :
    return(data)

def nilai(**data) :
    return(data)

def cetak(nilai) :
    print(nilai['nim'],nilai['nama'],nilai['nilai'])