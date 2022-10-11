import mysql.connector

aksesDb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="akademik"
)

kursor = aksesDb.cursor()

# sql = "create database akademik" #perintah sql

# kursor.execute(sql)

# sql = """ CREATE TABLE mahasiswa (
#           id INT AUTO_INCREMENT PRIMARY KEY,
#           nim VARCHAR(25),
#           nama VARCHAR(25),
#           prodi VARCHAR(2) ) """

print("Program Isi data Mahahasiswa")
id = input("Input ID ")
nim = input("Input NIM ")
nama = input("Input Nama ")
prodi = input("Input Prodi ")

sql = "INSERT INTO mahasiswa VALUE (%s,%s,%s,%s) "
val = (id,nim,nama,prodi)

kursor.execute(sql,val)
aksesDb.commit()

print(kursor.rowcount, " record tersimpan")
