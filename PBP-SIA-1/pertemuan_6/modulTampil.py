import os

def tampil(dataMahasiswa) :
    os.system("cls")
    print("Daftar Mahasiswa")
    for item in dataMahasiswa :
        print('{nim:10} {nama:15} {prodi:15}'.format(**item))
    input()