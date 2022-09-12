k = "l" # inisiasi nilai awal
while k != "s" : # mulai perulangan jika ditemukan tekan keyboard "s"
    a = int(input("Masukkan bilangan a ")) # input bilangan a
    b = int(input("Masukkan bilangan b ")) # input bilangan b
    c = a + b # proses c = a + b
    if c >= 5 : # jika c lebih dari 5 maka tampil keterangan "Nilai C lebih dari 5"
        print("Nilai C lebih dari 5")
    print(c) # output bilangan c
    k = input("Apakah akan selesai? [tekan s]") # isikan huruf "s"