def nilai(**data) :
    return(data)

def cetak(nilai) :
    print(nilai['nim'],nilai['nama'],nilai['nilai'])

mhs = nilai(nim="087",nama="Amir",nilai=67)
cetak(mhs)

mhs = nilai(nim="088",nama="Budi",nilai=70)
cetak(mhs)