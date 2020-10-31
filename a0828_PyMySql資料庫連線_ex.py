import pymysql
db = pymysql.connect(
    "localhost",
    "root",
    "root",
    "mdb",
    charset="utf8"
    )
cursor = db.cursor()
sql = "SELECT * FROM `emp`"
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    print(i)
db.commit()
db.close()

