import mysql.connector

dbPerpus = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)

# program perpustakaan
print("Program Isi Data Buku Perpustakaan")
kode = input("Kode Buku ")
judul = input("Judul Buku ")
pengarang = input("Pengarang Buku ")
penerbit = input("Penerbit Buku ")

kursor = dbPerpus.cursor()

sql = "insert into buku value (%s, %s, %s, %s)"
val = (kode,judul,pengarang,penerbit)
kursor.execute(sql,val)
dbPerpus.commit()
print(kursor.rowcount, " record tersimpan")



