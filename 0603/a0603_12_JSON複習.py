import json
with open('json_test3.json','r',encoding='utf8') as fin:
    f = json.load(fin)
f["name"] = "My Name"
print(f)
# with open('json_test3.json','w',encoding='utf8') as fout:
#     fout.write('{"sno":"1001","sna":"大鵬華城","tot":"38"}')
    # json.dump(f,fout)
    