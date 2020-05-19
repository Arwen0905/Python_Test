# 複習一遍
'''
import sqlite3
conn = sqlite3.connect('new3_Database.db')
sql = "CREATE TABLE IF NOT EXISTS `new2_table`(id INT AUTO_INCREMENT PRIMARY KEY,name TEXT,email TEXT)"
conn.execute(sql)
sql = "INSERT INTO `new2_table`(id,name,email) VALUES('NULL','大明','qqq@gmail.com')"
sursor = conn.execute(sql)
for t in sursor:
    print(t[0],t[1])

conn.commit()
conn.close()
'''
# 複習一遍
f = 0b11110110
print(f)
import pymysql
db = pymysql.connect(
'''
     "localhost","root",
     "123456",
     "data_base_one",
      charset="utf8"
'''
      )
cursor = db.cursor()
# sql = "SELECT * FROM table_one"
# sql = "SELECT COUNT(*) FROM table_customers"
# sql = "SELECT SUM(price) FROM table_customers"
# sql = "SELECT ASCII(name) FROM table_customers"
# sql = "SELECT CONCAT(name,'-',price) FROM table_customers"
# sql = "SELECT LENGTH(price) FROM table_customers"
sql = "SELECT REPLACE(name,'陳','林林林') FROM table_customers"
cursor.execute(sql)
data = cursor.fetchall()

for t in data:
    print(t)
    
try:
    cursor.execute(sql)
    db.commit()
    print('完成動作')
except:
    db.rollback()
    print('Erorrr！')
    
db.commit()
db.close()
