d = [
    {"user": "天龍啊德", "介紹":{"種族": "天龍人", "能力":"無限美金", "技能": "白白濃濃"}},
    {"user": "重灌阿瓜", "介紹":{"種族": "孤狼", "能力":"windows重灌", "技能": "刪除系統責罵免疫"}}, 
    {"user":"巨屎阿文", "介紹":{"種族": "首抽N卡", "能力":"常駐拉屎", "技能":"拉屎時間50分"}}
]
# 【多維字典小測試】
# d1,d2,d3,d4 = zip(*map(lambda d:(d['user'],d['介紹']['種族'],d['介紹']['能力'],d['介紹']['技能']),d))
# print(d1)
# print(d2)
# for i in d3:
#     print(i)

# 【挖取多維字典】
# cc = [{'user':'Arwen','技能':{'小招':'普通砍','遠程':'子彈'}},{'技能':'高級砍','遠程':'波動砲'}]
# print(cc[0].get('技能').get('遠程'))
# print(cc[1].get('遠程'),cc[1].get('技能'))

# 【多維字典小測試】
# lst = [
#       {'user':'Arwen','技能':{'近戰':'普通砍','遠程':'飛踢'}},
#       {'user':'Jackson','技能':{'近戰':'刺擊','遠程':'投石'}}
#       ]
# n1,n2,n3 = zip(*map(lambda n:(n['user'],n['技能']['近戰'],n['技能']['遠程']),lst))
# print(type(n1))
# print(n1,n2)
# print(n3[1])

# 【改編範例】
# 利用*號操作符，可以將元組解壓為列表。
# user, 種族, 能力, 技能 = zip(*map(lambda x: (x['user'], x['介紹']['種族'], x['介紹']['能力'], x['介紹']['技能']), d))
# print(type(user),list(user))
# print(type(種族),種族)
# print(type(能力),能力)
# print(type(技能),技能)

# f = lambda num1, num2: num1 if num1 > num2 else num2
# print(f(num2=15,num1=112))

# f = lambda start,stop = 10: [i for i in range(start,stop+1)]
# print(f(25,50))



# 【filter】
# 學生成績資料組
# scores = [90, 50, 80, 40, 100]
# f = lambda x:True if x < 60 else False
# fail_scores = filter(f,scores)
# for i in fail_scores:
#     print(i)

# fail_scores = filter(lambda x:True if x<60 else False,scores)
# print(list(fail_scores))
# ↑
# print(list(fail_scores))
# for i in fail_scores:
#     print(i)

# 建立篩選不及格成績的lambda函式
# f = lambda x: True if x < 60 else False

# 呼叫filter()函式，傳入篩選函式和資料組
# fail_scores = filter(f, scores) 

# 顯示篩選後的成績，執行結果：[50, 40]
# for item in fail_scores:
#     print(item)


# 【map】
# 顯示處理後的成績，執行結果：[50, 52, 54, 60, 60, 60]
# scores = [50, 52, 54, 56, 58, 60]
# new_scores = map(lambda x: 60 if 55 <= x < 60 else x, scores)
# print(scores)
# for item in new_scores:
    # print(item,end=',')

# 【zip就像是把多項資料給包裝起來】
# print('===============重點測試=================')
user = ['阿文','阿德','師傅','YO桑'] 
occupation = ['動畫設計','後端工程','前端工程','執行長']
age = [36,29,40,31]
skill = ['拉屎','黑肉','坐著','加拿大']
# =================================================================================================
dic = {'近況':{'學生':'職訓局','菲律賓':'高薪客服','備考':'日檢','離職':'創業'}}
print(type(dic))
print(dic.get('近況').get('菲律賓'))
print('!!!map進行 str轉換時，資料需要轉換成串列可傾倒出純字串')
world = map( str,[dic.get('近況').get('菲律賓'),dic.get('近況').get('學生')])
print(*world)

### 若要使用字典多維資料，可利用 zip、map、lambda ###
dict_test = [{'近況':{'學生':'職訓局','菲律賓':'高薪客服','備考':'日檢','離職':'創業'}}]
n1,n2,n3,n4 = zip(*map(lambda n:(n['近況']['學生'],n['近況']['菲律賓'],n['近況']['備考'],n['近況']['離職']),dict_test))
# print(type(n1))
# print(*zip(n1,n2),'<<<<<<<<')

print('===========最終測試版==============')
hello = map(str,n1+n2+n3+n4)
zip_deda = zip(user,age,occupation,hello) # zip就像包裝起來
print(*zip_deda,'<< 解壓') #擁有 * 解壓屬性
for i in zip_deda:
    print(i)
# print(type(zip_deda),'<型態>',zip_deda,'\n')
# print(*zip_deda,'<< 判斷:上面使用過，就無法呈現的BUG')


# print('=== 運用 map進行 def處理多筆資料運算，map(函數,資料) ===')
# lst1=[5,4,3,2,1]
# lst2=[1,2,3,4,5]
# def f(x):
#     return x*2
# print(f(lst2),' << fail') # 放串列，無法運算
# print(*map(f,lst2),' << 基本使用:map(f,lst2)') # 由右邊的(資料)，使用左邊的(func)功能
# print(list(map(f,lst2)),' << 轉串列') # 同上，只是轉成串列輸出
# print([f(x) for x in lst2]) # comprehensive 簡短語法
# print([f(x) for x in lst1+lst2]) #自行想的多組資料處理法


# print('=== 運用*map型態處理多組資料 ===')
# 注意! map處理的標準，是以最短資料列長度為主
# lst3=[1,2,3,4,5]
# lst4=[10,20,30,40,50]
# lst5=[100,200,300,400,500]
# def adder(x1,x2,x3):
#     ans= x1+x2+x3
#     return ans
# print(adder(50,50,50))
# print([adder(x,y,z) for x,y,z in zip(lst3,lst4,lst5)])
# print(*map(adder,lst3,lst4,lst5))

