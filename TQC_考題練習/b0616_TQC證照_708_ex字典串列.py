dic1 ={'3':'小明','1':'小花'}
dic2 ={'2':'阿冬','4':'小瓜'}
dic3 = dic1.copy()
dic3.update(dic2)
dic3 = sorted(dic3.items())
print(dic3)
print(type(dic3))
dic3 = dict(dic3)
print(dic3)
