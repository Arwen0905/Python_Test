import sqlite3 #模組
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
conn = sqlite3.connect('test.db')
print('Opened database successfully')
#建立 cursor(游標物件) 供資料庫後續操作
c = conn.cursor()

#sql語句指定一個sql變數
sql = '''CREATE TABLE `company1`\
    (id INT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address char(50),
    salary REAL);'''
#執行 SQL 指令
#建立資料表(create table)
c.execute(sql)
print('Table created successfully')
#執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
conn.commit()
#關閉資料庫(不會自動呼叫 commit())
conn.close()

#SQLite：
# →是包含在一個相對小的C程式庫中的關聯式資料庫管理系統。
# →不是一個用戶端/伺服器端結構的資料庫引擎。
# →被整合在用戶程式中，使用動態的SQL語法操作。
# →特性：
#     →支援交易ACID(單一性、一致性、孤立性、耐久性)
#     →無需設定與管理，因此若要管理，需要搭配第三方套件所提供的工具。
#     →支援ANSI-SQL92語法(資料庫查詢語言標準)
#     →資料庫系統是一個檔案。
#     →檔案大小最大支援到2TB。
#     →記憶體需求小：原始程式採用不到30000行的C語言撰寫，僅需要小於250KB的程式空間。
#     →免費使用。
#     →使用 unicode。

# #Python使用sqlite3模組(2.5版以上已內建)
# →使用方法：
#     →sqlite3.connect：開啟資料庫的連結，成功開啟則傳回一個連線物件。
#     →sqlite3.cursor：建立cursor(資料指標)
#     →sqlite3.execute：執行SQL語法
#     →sqlite3.commit：提交目前的交易(執行資料庫的操作)
#     →sqlite3.rollback：回復上一次呼叫commit()對資料庫的更改。
#     →sqlite3.close：關閉資料庫連結。

import pymysql
db = pymysql.Connect(
    'localhost',
    'root',
    '123456',
    'data_base_one',
    charset='utf8'
    )
cursor = db.cursor()
sql = 'SELECT * FROM `table_one`'
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    print(i)
db.commit()
db.close()
