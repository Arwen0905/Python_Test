import pymysql
db = pymysql.connect(
    "localhost",
    "root",
    "123456",
    "data_base_one",
    charset="utf8"
    )
cursor = db.cursor()
sql = "SELECT * FROM `table_two`"
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    print(i)
db.commit()
db.close()

