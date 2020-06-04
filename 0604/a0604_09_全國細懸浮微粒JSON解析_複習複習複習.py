import json
with open('全國細懸浮微粒手動監測資料.json',encoding='utf8') as fin:
    data = json.load(fin)
    # base = data['help']
    # base = data['success']
    base = data['result']['records']
    # print(base)
    for row in base:
        print(row['SiteName'],row['Concentration'])
    