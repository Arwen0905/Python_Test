dic = {}
print('Create dict1:')
while True:
  key = str(input('Key: '))
  if key == 'end':
    break
  dic.setdefault(key)
  value = str(input('Value: '))
  if value == 'end':
    break
  dic[key] = value
dic2 = {}
print('Create dict2:')
while True:
  key = str(input('Key: '))
  if key == 'end':
    break
  dic2.setdefault(key)
  value = str(input('Value: '))
  if value == 'end':
    break
  dic2[key] = value

dic3 = dic.copy()
dic3.update(dic2)
dic3_sort = sorted(dic3)

for i in dic3_sort:
    print(i,dic3[i])



# # dic3=dict(dic,**dic2)
# # dic3=(**dic,**dic2)
# # 常規迴圈寫入

