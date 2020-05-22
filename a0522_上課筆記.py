import pymysql
db = pymysql.connect(
    "localhost","root",
    "123456",
    "data_base_one",
    charset="utf8"
    )
# sql = str(input("請輸入欲查詢的資料表 : "))
sql = 'table_two'
print(sql)
cursor = db.cursor()
cursor.execute(f'SELECT * FROM {sql}')
data = cursor.fetchall()
for i in data:
    print(i)   
db.commit()
db.close()

import random
s=6
def output(s=6):
    count=1
    alst=[]
    while count<=6:
        alst.append(random.randint(1,100))
        print(alst)
        if len(alst) <= 1 :
            maxNum = alst[0]
            minNum = alst[0]
        else:
            if alst[-1] > maxNum:
                maxNum = alst[-1]
            elif alst[-1] < minNum:
                minNum = alst[-1]
        count+=1
    print('\n串列數字為:%s\n最大值:%d\n最小值:%d'%(alst,maxNum,minNum))
output(s)
'''
串列:list
轉換方式:
'''
    # └ 數組轉為串列 → 
tuple1=(1,2,3)
list1=list(tuple1)
print()
print(list1)
print(type(list1))

    # └ 串列轉為數組 → 
tuple2=tuple(list1)
print(tuple2)
print(type(tuple2))
dict1 = {1:'東尼',2:'妮妮'}
dict2 = {'蘋果':15,'香蕉':10,'番茄':12}
print(dict1)
print(dict2)
print(dict1.get(1))
print(dict2.get('蘋果'))
print(dict2.get('鳳梨')) #若無key，不會出錯

'''
=>字典(詞典):dict
    └ 建立:   鍵值1:值1
        └ 字典名稱={元素1,元素2,元素3,...}
dict可寫以下三種格式

# 二維詞典、三維詞典:
dict1([[key1:value1],[key2:value2],[key3:value3]])

# 正常版:
dict2(key1:value1,key2:value2,key3:value3)

# key值為字串:
dict3(str:value1,str:value2,str:value3)

資料結構整理:
    └ 字串元素無依定的順序排列 → 同學記憶體情境
      串列元素則為依序排列 → 記憶體
    └ 字典取值的方式: 字典名稱[key]
      以key(不可重複)作為索引取得 value(可重複)
      若重複，則將key覆蓋，只有最後的key會存在        
=>字典(詞典):dict
    └ 當key不存在，產生錯誤
    └ 使用get()以鍵取值
    字典名稱.get(key) <<<如果沒有key，不會出錯，只會有none
'''
# 字典查詢範例
dict3 = {
        'A':'說話很客氣，且有條有理，喜歡注視著對方的臉來說話，當聆聽對方講話時，則喜歡頻頻點頭，表示回應，有趣的是在講電話時，通常會不由自主的拿著筆在紙上亂畫。',
         'B':'說話時很風趣，常會『唱作俱佳，手舞足蹈』。十分幽默有趣，不過最好玩的是在說話時，一會兒坐、一會兒站、一會兒比手、一會兒畫腳，根本無法安靜坐在同一地方，這大概是他們天性活潑好動的原因吧！',
         'O':'說話態度強而有力、簡單明瞭，說到高興的時候還會習慣性地拍拍對方或觸碰對方的身體，因此奉勸Ｏ型的人，與人交談時儘量留意自身的舉動。',
         'AB':'口才很好，談話內豐富又有趣，而也很有耐心聽人把話講完，可說是最佳的談天對象。'}
# t = input('請輸入血型')
t = 'O'
blood = dict3.get(t)
if blood == None:
    print('沒有這個血型')
else:
    # print(str(dict3[blood]))
    print(blood)
'''
=>字典修改:
    字典名稱[key]=value
    └ 字典刪除:
        └ 刪除特定元素: del 字典名稱[key]
        └ 刪除所有元素: 字典名稱.clear()
        └ 刪除字典: del 字典名稱
'''
print(dict2,'<<<還沒')
# del dict3[香蕉]
# dict3.clear() # 會變成{}
print(dict2,'<<<刪除了')
'''
【已存在的資料】
請輸入學生姓名:李大年
李大年的成績為:67
【尚未存在的資料】
請輸入學生成績:陳美玲
輸入學生分數:80
印出字典內容...
【學生不存在字典中，輸入資料後加入字典】
'''
# dict3 = {'李大年':'67'}
# n = input('請輸入姓名: ')
# c = input('請輸入分數: ')
# dict3.setdefault(n,c)
# print(dict3)
# 輸入學生姓名，判斷有無在字典裏面，並加入其中-------------------------------------------------
dict4 = {'李大年':'67'}
# name = input('輸入學生姓名: ')
name = '冬瓜明'
if name in dict4:
    print(name,',',str(dict4[name]))
else:
    # score = input('輸入學生分數: ')
    score = 90
    dict4[name] = score
    print(name,',',str(dict4[name]))
    print(name,',',str(dict4.get(name)))
# -------------------------------------------------
# !注意get與dict[name]的使用!
# └ 使用get()以鍵取值
# └ 使用dict[name] 以方括弧的[鍵]取值
'''
【字串(str)】
=> python 並無特別區分字元及字串，均已單、雙引號前後括住
=> 建立空字串:
    s1=str()
    s2=''
=>建立字串
    s3=str('這是python程式設計')
    s4=str('hello python')

=>len(字串名):字串長度(字元數)
=>max(字串名):字串最大值
=>min(字串名):字串最小值
=>[位置數值]:取得字串特定字元
    字串名[位置數值] ※從0開始算
    s4[3],s4[-5]
              └ 若為負值，則加上字串長度
=>[起始值:終止值]
    取得從起始~終止值-1的子字串
    字串名[起始值:終止值]
    s4[3:8] → gy is
'''
s1=str()
s2=''
s3=str('這是python程式設計')
s4=str('today is rainy day')
print(s1,s2,s3,s4,sep=',',end='')
print()
print(len(s3)) # 取得長度
print(max(s3)) # 取最大值字元
print(min(s3)) # 取最小值字元
print(s3[2:-2]) # 取得該位置顯示出
print(s4[-5]) # 若為負值，則加上字串長度
print(s4[3:8]) # 取得從起始~終止值-1的子字串
'''
【字串(str)】
=> + :串接
=> * :複製
'''
s5='Simon'
s6='lee'
print(s5+s6) # 字串相加
print(s5*2) # 複製兩次
'''
【字串(str)】
字串測試:字串名.函式()
函式():傳回值為布林值
    └ isalnum():字串是否為字元及數值
'''
s6 = 'simon'
print(s6.isalnum(),'是否為字元') # 字串是否為字元
print(s6.isdigit(),'是否為數值') # 字串是否為數值
print(s6.islower(),'是否為英文小寫') # 字串是否皆為英文小寫
print(s6.isupper(),'是否為英文大寫') # 字串是否皆為英文大寫
print(s6.isspace(),'是否為空白字元') # 字串是否皆為空白字元
'''
【字串(str)】
=> 子字串:
    └ startswith('子字串'):字串開頭是否為子字串
    └ endswith('子字串'):字串尾端是否為子字串
    └ find('子字串'):字串中子字串的最小位置數值
    └ rfind('子字串'):字串中子字串的最大位置數值
    └ count('子字串'):字串中子字串的個數
'''
print(s5.startswith('Si')) # 注意判斷會吃大小寫
print(s5.endswith('on')) # 判斷字串中尾端是否為('子字串')
print(s5.find('o')) # 判斷字串中最小位置數值，起始0開始，沒有則顯示-1
print(s5.find('沒')) # 開頭加" r "為判斷字串最大位置數值
s7 = 'abcdeabcde'
print(s7.rfind('e')) # 判斷字串中最大位置數值，最大測試 \\9，不是4
print(s7.count('e')) # 判斷字串中子字串個數
'''
5/22 下午
【字串(str)】
=> 字串轉換:
    └ capitalize():將字串中第一個字元轉換為大寫，其餘為小寫
        ※字串名.capitalze()
    └ lower():將字串中所有字元轉換為小寫
    └ upper():將字串中所有字元轉換為大寫
        ※字串名.lower()
        ※字串名.upper()
    └ swapcase():將字串中的字元大寫轉換為小寫；小寫轉換為大寫
        ※字串名.swapcase()
    └ replace(str1,str2):
        將 str1 以 str2 取代
        ※字串名.replace(str1,str2)
    └ title():將字串中每一個單字為第一個字元轉換為大寫，其餘為小寫
        ※字串名.title()
'''
s8='welcome to taipei'
s8 = s8.replace('taipei', 'taiwan' +'\n             ↑↑↑ replace字串函式: 將台北替換為台灣')
print(s8)
print()
'''
【字串(str)】
=> 空白處理:字串名.函式()
    └ lstrip(): 刪除字串"左側"空白
    └ rstrip(): 刪除字串"右側"空白
    └ slstrip(): 刪除字串"左右側"空白
'''
s9 ='    welcome to taipei    '
print(s9,' <<< 原型字串(s9)，注意空白處')
s9 = s9.lstrip()
print(s9,' <<< 刪右邊')
s9 ='    welcome to taipei    '
s9 = s9.rstrip()
print(s9,' <<< 刪左邊')
s9 ='    welcome to taipei    '
s9 = s9.strip()
print(s9,' <<< 左右都刪')
'''
【字串(str)】
=> 對齊:
    └ cemter(寬度值):
        將字串以寬度值置中對齊
    └ ljust(寬度值):
        將字串以寬度值靠左對齊
    └ rjust(寬度值):
        將字串以寬度值靠右對齊
'''
s10 = 'Taipei City'
s100 = '123456789012345678901234567890'
print(s100)
print(s10.center(30))
s10 = 'Taipei City'
print(s10.ljust(30))
s10 = 'Taipei City'
print(s10.rjust(30))
'''
【字串(str)】
=> split():字串分割
    └ 以空白字元作為分割字元
    split('-'):指定分割
    └ 以字串 or符號指定該元素為"分割要素"
'''
s11 = 'apple banana kiwi orange'
lst = s11.split()
print(lst)
s12 = '05-22-2020'
lst1 = s12.split('-')
print(lst1)
