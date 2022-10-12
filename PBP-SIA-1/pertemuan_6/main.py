import os
from modulEntry import entry
from modulTampil import tampil

pilihMenu = "" 
dataMahasiswa = []
while pilihMenu != "x" :
    os.system("cls")
    print("Program Olah Data Mahasiswa")
    print("Menu : ")
    print("1. Entry Data Mahasiswa")
    print("2. Tampil Daftar Mahasiswa")
    print("x. Keluar dari program")
    pilihMenu = input("Menu yang dipilih : ")
    if pilihMenu == "1" :
        dataMahasiswa = entry(dataMahasiswa)
    elif pilihMenu == "2" :
        tampil(dataMahasiswa)

    