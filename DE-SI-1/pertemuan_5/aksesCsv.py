import csv 
# tambah data
fileSimpan = open('mahasiswa.csv','a')
barisBaru = "\n016, deni, Informatika"
fileSimpan.write(barisBaru)
fileSimpan.close()

#output
file = open('mahasiswa.csv', 'r') 
reader = csv.reader(file) 
print(reader)
for row in reader:
   print(" {:10} {:10} {:10} ".format(row[0],row[1],row[2])) 
file.close()
