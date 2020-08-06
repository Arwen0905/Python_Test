import sqlite3
conn = sqlite3.connect('lotto649_BrowserDB2.db')
c = conn.cursor()
print('資料庫打開了!')
#執行 SQL指令
# c.execute("SELECT FROM `company1` where id=2")
c.execute("SELECT * FROM `lotto649_2014`")
conn.commit()
print(conn.total_changes)
# cursor = conn.execute("SELECT 獎號1 FROM *")

#關閉資料庫(不會自動呼叫 commit())
conn.close() #資料庫關閉
print('資料庫關閉了！！！')
