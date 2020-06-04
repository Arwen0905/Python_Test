import sqlite3
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
conn = sqlite3.connect('test.db')
#建立 cursor(游標物件) 供資料庫後續操作
c = conn.cursor()
print('Opened database successfully')
#執行 SQL 指令
#新增記錄(insert into)
c.execute("INSERT INTO `company1`(id,name,age,address,salary)\
          VALUES(1,'Paul',32,'California',20000.00)");
c.execute("INSERT INTO `company1`(id,name,age,address,salary)\
          VALUES(2,'Paul',25,'texas',15000.00)");
c.execute("INSERT INTO `company1`(id,name,age,address,salary)\
          VALUES(3,'Paul',23,'Norway',20000.00)");
c.execute("INSERT INTO `company1`(id,name,age,address,salary)\
          VALUES(4,'Paul',25,'Rich-Mond',65000.00)");
#執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
conn.commit()
#關閉資料庫(不會自動呼叫 commit())
conn.close()
