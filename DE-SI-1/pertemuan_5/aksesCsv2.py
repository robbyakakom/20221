import csv 
# tambah data
file = open('../barang.csv','r')
reader = csv.reader(file,delimiter=';') 
print(reader)
for row in reader:
   print(" {:10} {:10} {:10} ".format(row[0],row[1],row[2])) 