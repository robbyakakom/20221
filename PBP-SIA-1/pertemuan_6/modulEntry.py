import os

def entry(dataMahasiswa) :
    ulang = "Y"
    while(ulang == "Y") :
        os.system("cls")
        print("Entry data mahasiswa")
        nim = input("NIM ? ")
        nama = input("Nama Mahasiswa ? ")
        prodi = input("Program Studi ? ")
        dataMahasiswa.append({'nim':nim,'nama':nama,'prodi':prodi})
        ulang = input("Apakah akan isi data lagi ? ")
    return dataMahasiswa