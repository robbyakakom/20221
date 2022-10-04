import csv 
file = open('mahasiswa.csv', 'r') 
hasil = csv.reader(file) 

print("{:10} {:15} {:10} ".format("NIM","Nama Mahasiswa","Prodi"))
baris = 0
for mhs in hasil :
    baris = baris + 1
    if baris == 1 :
        continue
    nim = mhs[0]
    nama = mhs[1]
    prodi = mhs[2]
    print("{:10} {:15} {:10} ".format(nim, nama, prodi))
    
