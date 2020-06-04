import json
with open('ubike_1.json',encoding='utf8') as fin:
    data = json.load(fin)
    print(data)