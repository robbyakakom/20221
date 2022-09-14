a = int(input("masukkan nilai 1 "))
b = int(input("masukkan nilai 2 "))
c = a + b
print("hasil nilai 3 " + str(c))

# jika c > 80 maka keterangan Baik
# jika c > 40 dan c < 79 maka keterangan Cukup
# selain itu maka keterangan Kurang

# print("Baik") if c > 80 else print("Kurang")
if c > 80 :
    print("Baik")
elif c > 40 and c < 79 :
    print("Cukup")
else :
    print("Kurang")


# nama = input("Masukkan nama Anda ?")
# print("Nama " + nama)

