import sqlite3 #模組
conn = sqlite3.connect('test.db') #連結資料庫
#建立 cursor(游標物件) 供資料庫後續操作
c = conn.cursor() #資料庫指定變數
print('打開資料庫了！！！')
#更新記錄(update set)，更新 資料表 設定 薪水1千萬-1塊 目標條件為 id=1
c.execute("UPDATE `company1` set salary=9999999.00 where id=1")
conn.commit() #確定執行
# print('查詢語法 conn.total_changes 看有多少資訊做更新')
#conn.total_changes：取得資料庫改變(修改、新增)的總次數。
print('total number of rows updated: ',conn.total_changes)
# 執行與變數一起設定，指定了 cursor變數做sql語法
cursor = conn.execute("SELECT id,name,address,salary FROM company1")
for row in cursor: #挖出來
    print('id = ',row[0])
    print('name = ',row[1])
    print('address = ',row[2])
    print('salary = ',row[3])
    print('──────────────────────────────────────')
    
#關閉資料庫(不會自動呼叫 commit())
conn.close() #資料庫關閉
print('資料庫關閉了！！！')
