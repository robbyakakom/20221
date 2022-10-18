import mysql.connector

#olap_db database
dbOlapDb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="olap_db"
)
kursorOlapDb = dbOlapDb.cursor()

# sql = """
#         select d_suplier.suplier, d_bulan.bulan, d_produk.produk, f_pembelian.jumlah, f_pembelian.harga
#         from f_pembelian
#         inner join d_suplier on d_suplier.id_suplier = f_pembelian.id_suplier
#         inner join d_bulan on d_bulan.id_bulan = f_pembelian.id_bulan
#         inner join d_produk on d_produk.id_produk = f_pembelian.id_produk
#         where d_suplier.id_suplier = 2 and d_bulan.id_bulan = 4
# """
sql = """
        select d_bulan.bulan, sum(f_pembelian.jumlah)
        from f_pembelian
        inner join d_suplier on d_suplier.id_suplier = f_pembelian.id_suplier
        inner join d_bulan on d_bulan.id_bulan = f_pembelian.id_bulan
        inner join d_produk on d_produk.id_produk = f_pembelian.id_produk
        group by d_bulan.bulan

"""
# sql = """
#         select d_suplier.suplier, max(f_pembelian.jumlah)
#         from f_pembelian
#         inner join d_suplier on d_suplier.id_suplier = f_pembelian.id_suplier
#         inner join d_bulan on d_bulan.id_bulan = f_pembelian.id_bulan
#         inner join d_produk on d_produk.id_produk = f_pembelian.id_produk
# """
kursorOlapDb.execute(sql)
hasil = kursorOlapDb.fetchall()
for row in hasil :
    print(row)

