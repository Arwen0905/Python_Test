import json
with open('全國細懸浮微粒手動監測資料.json',encoding="utf8") as fin:
    data = json.load(fin)
    base = data['result']['records']
    for row in base:
        # print(row)
        # print(row['SiteName'],row['Concentration'],row['ItemUnit'])
        print('測站:(%s)--縣市 (%s)--PM2.5 = %s'%(row['SiteName'],row['Concentration'],row['ItemUnit']))
        