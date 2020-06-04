import json
with open('全國細懸浮微粒手動監測資料.json',encoding="utf-8") as fin:
    data = json.load(fin)
    base = data['result']['records']
    # print(base)
    for row in base:
        # print(row['SiteName'])
        print('測站 (%s) 縣市PM2.5值為: %s'%(row['SiteName'],row['Concentration']))
        