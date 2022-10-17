import mysql.connector

#northwind database
dbNorthwind= mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="northwind"
)
kursorNorthwind = dbNorthwind.cursor()

#olap_db database
dbOlapDb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
)
kursorOlapDb = dbOlapDb.cursor()

#mebuat database olap_db
sql = "drop database if exists olap_db"
kursorOlapDb.execute(sql)
sql = "create database olap_db"
kursorOlapDb.execute(sql)

#memilih database
sql = "use olap_db"
kursorOlapDb.execute(sql)

#membuat tabel dimensi produk
sql = """
        create table d_produk (
            id_produk int primary key,
            produk varchar(50)
        )
"""
kursorOlapDb.execute(sql)

#membuat tabel dimensi suplier
sql = """
        create table d_suplier (
            id_suplier int primary key,
            suplier varchar(50)
        )
"""
kursorOlapDb.execute(sql)

#membuat tabel dimensi bulan
sql = """
        create table d_bulan (
            id_bulan int primary key,
            bulan varchar(50)
        )
"""
kursorOlapDb.execute(sql)

#membuat tabel fact pembelian
sql = """
        create table f_pembelian (
            id_suplier int,
            id_bulan int,
            id_produk int,
            jumlah varchar(50),
            harga varchar(50),
            constraint fk_suplier foreign key(id_suplier) references d_suplier(id_suplier),
            constraint fk_bulan foreign key(id_bulan) references d_bulan(id_bulan),
            constraint fk_produk foreign key(id_produk) references d_produk(id_produk)
        )
"""
kursorOlapDb.execute(sql)

#ekstrak produk
sql = "select id as id_produk, product_name as produk from products"
kursorNorthwind.execute(sql)
produk = kursorNorthwind.fetchall()
#load produk
for item in produk :
  sql = "insert into d_produk (id_produk, produk) value (%s, %s) "
  val = (item[0],item[1])
  kursorOlapDb.execute(sql,val)

#ekstrak suplier
sql = "select id as id_suplier, company as suplier from suppliers"
kursorNorthwind.execute(sql)
suplier = kursorNorthwind.fetchall()
#load suplier
for item in suplier :
  sql = "insert into d_suplier (id_suplier, suplier) value (%s, %s) "
  val = (item[0],item[1])
  kursorOlapDb.execute(sql,val)

#ekstrak bulan
bulan = (
  [1,"Januari"],
  [2,"Februari"],
  [3,"Maret"],
  [4,"April"],
  [5,"Mei"],
  [6,"Juni"],
  [7,"Juli"],
  [8,"Agustus"],
  [9,"September"],
  [10,"Oktober"],
  [11,"Nopember"],
  [12,"Desember"]
)
#load bulan
sql = "insert into d_bulan (id_bulan,bulan) value (%s,%s)"
val = bulan
kursorOlapDb.executemany(sql,val)

#ekstrak pembelian
sql = """select 
         purchase_orders.supplier_id as id_suplier,
         DATE_FORMAT(purchase_orders.creation_date,"%c") as id_bulan,
         purchase_order_details.product_id as id_produk,
         sum(purchase_order_details.quantity) as jumlah,
         sum(products.list_price) as harga
         from purchase_orders
         inner join purchase_order_details on purchase_orders.id = purchase_order_details.purchase_order_id
         inner join products on products.id = purchase_order_details.product_id
         group by purchase_orders.supplier_id, DATE_FORMAT(purchase_orders.creation_date,"%c"), purchase_order_details.product_id         """
kursorNorthwind.execute(sql)
pembelian = kursorNorthwind.fetchall()
#load pembelian
for item in pembelian :
  sql = "insert into f_pembelian (id_suplier,id_bulan, id_produk,jumlah,harga) value (%s, %s, %s, %s, %s) "
  val = (item[0],item[1],item[2],item[3],item[4])
  kursorOlapDb.execute(sql,val)

dbOlapDb.commit()

sql = "show tables"
kursorOlapDb.execute(sql)
hasil = kursorOlapDb.fetchall()
print(hasil)

