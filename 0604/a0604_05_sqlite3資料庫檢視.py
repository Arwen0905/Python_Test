import sqlite3
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
conn = sqlite3.connect('test.db')
#建立 cursor(游標物件) 供資料庫後續操作
c = conn.cursor()
print('Opened database successfully')
#執行 SQL 指令
#查詢記錄(select)
cursor = c.execute("SELECT id,name,address,salary FROM company1")
# 簡易撈出來
# for i in cursor:
#     print(i)
#以 cursor 物件c 執行 SQL 查詢指令後，得到查詢結果，設定給變數 cursor
#以迴圈將查詢結果 cursor 中每一筆記錄取出(row物件)，
#再以索引將記錄的欄位資料取得後，設定給對應的變數做 輸出顯示。
for row in cursor:
    print('id = ',row[0])
    print('name = ',row[1])
    print('address = ',row[2])
    print('salary = ',row[3])
    print('──────────────────────────────────────')

#關閉資料庫(不會自動呼叫 commit())
conn.commit()
print('Operatioin done successfully')
