berhenti = "l"
while berhenti != "s" :
    ## penggunaan pemilihan / kondisicld
    nilai = int(input("Isi nilai Anda ? "))

    # jika nilai >= 75 keterangan Baik
    # jika nilai antara 40 sampai 74 keterangan Cukup
    # selain itu keterangan Kurang
    if nilai >= 75 :
        print("Baik")
    elif nilai >= 40 and nilai < 75 :
        print("Cukup")
    else :
        print("Kurang")
    print("")
    berhenti = input("Ketik s untuk berhenti ! ")