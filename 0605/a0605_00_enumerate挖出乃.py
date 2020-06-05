print('{}{}{}'.format('a','b','c'))
a1 = [1,2,3,4,5,6]
a2 = ['開頭','蘋果','香蕉','西瓜','奇異果','結束']
for index,value in enumerate(a1):
    print('%d,%d'%(index,value))
for 索引值,裡面裝了啥 in enumerate(a2):
    print('索引[%-2d]:值[%-3s]'%(索引值,裡面裝了啥))

import json
with open ('../0604/全國細懸浮微粒手動監測資料.json',encoding="utf8") as fin:
    f = json.load(fin)
    data = f['result']['records']
    for index,i in enumerate(data):
        print(f['result']['records'][index])
