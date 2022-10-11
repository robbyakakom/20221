import mysql.connector

dbPerpus = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)

kursor = dbPerpus.cursor()

sql = """ create table buku (
            kode_buku varchar(10),
            judul_buku varchar(50),
            pengarang varchar(25),
            penerbit varchar(25) 
        ) """

kursor.execute(sql)


