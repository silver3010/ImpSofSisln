import sqlite3
from DataBaseManager import DataBaseManager

dataBaseManager = DataBaseManager()


con = sqlite3.connect(dataBaseManager.database)
materia=(11,'matematicas','Bañuelos Garcia Karen Yesenia',9)
if dataBaseManager.is_an_existing_materia(con, materia):
   print("ya existe el registro")
else:
    dataBaseManager.create_materia(con, materia)
cur = con.cursor()
cur.execute("Select * from materias;")
table_list = cur.fetchall()
for row in table_list:
    print(row)
con.close()