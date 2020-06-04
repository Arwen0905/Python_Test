import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
print('資料庫打開了!')
#執行 SQL指令
#刪除紀錄(delete)
c.execute("DELETE FROM `company1` where id=2")
conn.commit()
print('total number of rows deleted',conn.total_changes)
cursor = conn.execute("SELECT id,name,age,address,salary FROM company1")
for row in cursor:
    print('id = ',row[0])
    print('name = ',row[1])
    print('address = ',row[2])
    print('salary = ',row[3])
    print('──────────────────────────────────────')
#關閉資料庫(不會自動呼叫 commit())
conn.close() #資料庫關閉
print('資料庫關閉了！！！')
