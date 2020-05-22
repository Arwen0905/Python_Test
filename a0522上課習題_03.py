import random
# randLst = []
# count = 1
# while count <= 100:
#     num = random.randint(1, 1000)
#     if num not in randLst:
#         randLst.append(num)
#         count += 1
# randLst.sort(reverse=True)
# print('\n隨機100位數字產生器\n',randLst)
# print()
# print('第二大值為:',randLst[1])
# print('第二小值為:',randLst[-2])
# '''
# 老師提供 map() print(多寫)入技巧 -----------------------
# '''
# a,b,c = map(int,input('請輸入數字: (可多筆，中間需空格)').split())
# print(a,b,c)
# '''
# 可補充後續寫法
# '''
# '''
# 老師解題
# '''
randlst = []
count = 1
while count <= 100:
    Num = random.randint(1,100)
    if Num not in randlst:
        randlst.append(Num)
        count+=1
randlst.sort()
for j in range(1,101):
    if j % 10 == 0:
        print('%4d ' % (randlst[j-1]))
    else:
        print('%4d ' % (randlst[j-1]),end='')
print()
print(randlst[1])
print(randlst[len(randlst)-2])
