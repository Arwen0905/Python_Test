
dict1 = {'5':'小明','2':'大冬'}
dict2 = {'1':'小明','4':'小花'}
 
merge_dict = dict1.copy()
merge_dict.update(dict2)
merge_sort = sorted(merge_dict)
print(merge_sort)
for i in merge_sort:
    print('%s: %s'%(i,merge_dict[i]))
####### 輸出字串、soered()的使用、輸出時的字典指定觀念 #######

dic3 = dict1.copy()
dic3.update(dict2)
print('=== 測試lambda ===')
print(sorted(dic3.items(),key=lambda item:item[0]))
print(sorted(dic3.items(),key=lambda item:item[1]))

