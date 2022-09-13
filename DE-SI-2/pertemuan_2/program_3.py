## penggunaan pemilihan / kondisi
nilai = int(input("Isi nilai Anda ? "))

# if nilai > 60 :
#    print("Lulus")
# else :
#    print("Tidak Lulus")

# print("Lulus") if nilai > 60 else print("Tidak Lulus")

# jika nilai >= 75 keterangan Baik
# jika nilai antara 40 sampai 74 keterangan Cukup
# selain itu keterangan Kurang
if nilai >= 75 :
    print("Baik")
elif nilai >= 40 and nilai < 75 :
    print("Cukup")
else :
    print("Kurang")