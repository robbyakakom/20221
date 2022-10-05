#program utama
from subfolder.fungsi import jumlah
from subfolder.fungsi import kurang

bil_a = int(input("isi bilangan A "))
bil_b = int(input("isi bilangan B "))

jum = jumlah(bil_a,bil_b)
kur = kurang(bil_a,bil_b)

print("Hasil Jumlah ", jum)
print("Hasil Kurang ", kur)
