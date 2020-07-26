# 載入 json 與 csv 模組
import json
import csv

# 讀取 json 檔案並指定編碼為 utf8
with open("read_101.json", encoding='utf-8') as file:
    data = json.load(file)
    print(data[:1])
# 寫入 csv 檔案並指定編碼為 utf8
with open("write_101.csv", "w+", encoding='utf-8') as file:
    csv_file = csv.writer(file)
    for row in data:
        csv_file.writerow([row["title"],row["showUnit"],row["startDate"],row["endDate"]])
    
    # 寫入 title（活動名稱）、showUnit（演出單位）、startDate（活動起始日期）、
    # endDate（活動結束日期）等四個欄位