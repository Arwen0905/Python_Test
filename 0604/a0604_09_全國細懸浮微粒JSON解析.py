import json
with open('全國細懸浮微粒手動監測資料.json',encoding="utf-8") as fin:
    data = json.load(fin)
    for row in data:
        print(row)
        # print('測站 [%s] 縣市的PM2.5值為: %s'%(row[0],row[2]))