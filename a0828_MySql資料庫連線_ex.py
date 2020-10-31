import mysql.connector
maxdb = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "root",
  database = "lotto649",
  # database = "mdb",
  )
cursor=maxdb.cursor()

sql = "SELECT * FROM lotto649_2019"
# sql = "SELECT * FROM `emp`"
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    print(i)
maxdb.commit()
maxdb.close()

