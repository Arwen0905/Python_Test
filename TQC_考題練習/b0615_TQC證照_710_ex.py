#TODO
dic={}
while True:
    key = str(input("Key: "))
    if key == 'end':
        break
    value = str(input("Value: "))
    if value == 'end':
        break
    dic[key]=value

s = str(input('Search key: '))
print(s in dic)

