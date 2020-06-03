import json #載入JSON套件
#JavaScript 開放資料交換格式
#json 為JavaScript程式的一個子集合
print(json.dumps(['two',{'bar':('jaz',None, 2.0, 1)}]))
print(json.dumps("\"two\bar"))
print(json.dumps('u4321'))
print(json.dumps('\\'))
print(json.dumps({'c':0,'b':0,'d':0}, sort_keys=True))
                     #※ JSON排序指令: sort_keys=True
print(json.dumps([0,1,2,3,{'4':5,'6':7}],separators=(',',':')))
                    #※ JSON分隔符號: separators=(',',':)
print(json.dumps({'4':5,'6':7},sort_keys=True,indent=3))
#json.dumps()：將Python中的文件序列化為json格式字串
#json.loads()：為json.dumps()的反向，將已編碼的json字串解碼為Python物件
d1={'b':789,'c':456,'a':123}
print(json.dumps(d1,indent=4)) # ※以json排序法
d2=json.dumps(d1,sort_keys=True,indent=4)
print(d2)

# 資料格式如下：
# menu = \
#   {
#   "breakfast" : {
#       "hours": "7-10",
#       "items": {
#     "breakfast burritos": "$60",
#     "pancakes": "$35"
#   }
#       },
#   "lunch" : {
#    .....
#   }
#       },
#   "dinner" : {
#     .....
#   }
#       }
# }