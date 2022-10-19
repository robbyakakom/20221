class matematika :
    jumlahProses = 0
    def __init__(self,a,b) :
        self.a = a
        self.b = b
        matematika.jumlahProses += 1

    def tambah(self) :
        return self.a + self.b

#instantiasi
a = 10
b = 20
proses1 =  matematika(a,b)
print(proses1.tambah())
proses1.b = 400

proses2 = matematika(100,200)
print(proses2.tambah())

print(proses1.b)

print(matematika.jumlahProses)
# del proses1 

# print(proses1.b)

