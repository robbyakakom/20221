import mysql.connector

dbPerpus = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)

kursor = dbPerpus.cursor()

sql = "select * from buku"
kursor.execute(sql)
hasil = kursor.fetchall()

for row in hasil :
  print("Kode Buku : ", row[0])
  print("Judul Buku : ", row[1])
  print("Pengarang Buku : ", row[2])
  print("Penerbit Buku : ", row[3])



