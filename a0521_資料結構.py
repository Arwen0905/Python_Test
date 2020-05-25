list1 = []
list2 = [1,2,3,4,5]
list3 = ['頭','肩膀','身體','褲子','尾']
list4 = [1,35,16.78,'pineapple']
list1.append(10)
list1.append(20)
list1.insert(1,30)
print(list1 ,' <<<<<<<<<<<指定位置插入')
print(list2[1:3], '<<<<<<<<<<<<<指秀序列1至3以前')
print(len(list2))
print(list4)
print(list3)
list3.pop(0)
print(list3,' <<<<<<<<<< 頭不見了')
list2.pop(1)
print(list2)
list2.remove(3)
list2.remove(5)
print(list2 ,' <<< REMOVE 標示"名稱"刪除')
list3.append('apple')
list3.append('banana')
list3.append('orange')
print(list3,'新增字串 apple,banana,orange')
print(list3.count('apple'), '<<<<<<<<< count查數量有幾個')
print(list3.index('apple'), '<<<<<<<<< index查位置在哪裡')
list1.append(40)
print(list1 ,'新增40字碼')
list1.sort()
print(list1 ,'<<< 正排序')
list1.reverse()
print(list1 ,'<<< 反排序')
print(30 in list1 ,'<<< 30 有在裡面')
print(80 not in list1 ,'<<< 80 沒有在裡面')
print(sum(list1) ,'<<< 總和')
print(max(list1) ,'<<< 取最大值')
print(min(list1) ,'<<< 取最小值')
print(list1+list2 ,'<<< 元素相加')
print(2*list2 ,'<<< 元素乘以兩倍')
print()
print(list1 ,'<<< 本來的list1')
print(list1[-1] ,'<<< [-1]')
print(list1[-4:4] ,'<<< [-4:4]')
print(list2 ,'<<< 本來的list2')
print(list2[-1] ,'<<< [-1]')
list3 = ['apple','banana','orange','kiwi']
print(list3 , '<<< 新建的list3')
print()
for i in range(len(list3)):
    print('list3[%d]=%s' % (i,list3[i]))
print()
n=0
for l in list3:
    print(f'list3[{n}]={l}')
    n += 1

# lotto = []
# for i in range(1,7): # 轉六個數字
#     randNum = random.randint(1, 49) # 隨機 1-49個數字
#     print(lotto) 
#     lotto.append(randNum) # 將上述隨機數字append進入lotto變數
# print('樂透號碼式: ')
# for i in lotto:
#     lotto.sort() # 正排序
#     print('%4d'% i , end='')
# -----------------------------------------------------------
import random
lotto = []
checkNum = []
for i in range(0,50):
    checkNum.append(0)
    # print(checkNum) # 將欲隨機給予的值，先全部設定為"0"
count = 1 # 預設第一次判斷開始
while count<=6: # 設定判斷6次(樂透六碼)，開始設定
    randNum = random.randint(1, 49) # 給予樂透1個號碼 (1~49)
    print(randNum, '<<< 隨機一碼')
    # 假設給了一碼，進入以下判斷
    if checkNum[randNum] == 0: # 判斷該位置是否為0，進入以下程序
        lotto.append(randNum) # 在樂透陣列裡，填入亂數給予的數字
        count += 1 # 確認填入，已判斷的次數+1次
        print(checkNum)
    checkNum[randNum] = 1 # 該索引的位置改為1後，即表示該數字已用過!
    print('樂透號碼是:\n', end='')
for i in lotto:
    lotto.sort()
    print(i,end=' ')
print()

lotto = []
n = 1 # 預設第一次進入判斷
while n<=6: #共會給予六次判斷
    randNum = random.randint(1, 49) # 隨機一碼
    if randNum not in lotto: # 如果隨機一碼不在lotto裡的話進入以下處理
        lotto.append(randNum) #將不重複的隨機一碼，填入lotto陣列
        n+=1 # 判斷次數+1
print('樂透號碼是: \n' , end='')
lotto.sort()
for i in lotto:
    print(i,end=' ')
print()
lotto.sort()
print('號碼排序後: ')
for i in lotto:
    print('%4d' % i,end=' ')
print()
# -----------------------------------------------
#(TQC+)二維串列
# -----------------------------------------------
lst = [[1,2,3],[4,5,6]]
print(lst)
print(lst[0])
print(len(lst))
print(len(lst[0]))
# -----------------------------------------------
list5 = [[1,2,3],[4,5,6,7,8,9,10],[11,12]]
print(list5)
print(list5[0])
print(len(list5),'<<< len(list5) 查找數量')
print(len(list5[1]), '<<< len(list5[1]) 查找list5裡面的陣列數量')
# -----------------------------------------------
listTwo = []
# row = eval(input('輸入一維數量'))
# col = eval(input('輸入二維數量'))
row = 3
col = 3
listTwo = []
for i in range(row):
    listTwo.append([])
    for j in range(col):
        listTwo[i].append(random.randint(1,10))
print()
print(listTwo)
print()
# 加入二維序列，並計算總合
for col in range(len(listTwo[0])):
    total = 0
    for row in range(len(listTwo)):
        total += listTwo[col][row]
        print('第 %d 列的總和: %d' % (col,total))
print()
# -----------------------------------------------
tu1 = (1,2,3,4,5,6)
print(tu1)
tu2 = ()
print(tu2)
tu3 = tuple([x for x in range(1,6)]) 
    # ↑ tuple(...) <<這邊小括號是"中括號的結構"
print(tu3)
tu4 = tuple('python 你好') # 拆分字串，類似split
print(tu4)
tu1 +=(6,7) # 填入數值
print(tu1)
print(tu1[3:6]) # 指定位置，顯示元素
tu3 = 2*tu3
print(tu3)
print()
for i in tu1:
    print(tu1[i],end=' ')

print(tu1,'<<< tu1')
del tu1
# print(tu1)
#集合 -----------------------------------------------
s1 = {1,2,3}
s2 = set()
s3 = set([x for x in range(1,6)])
s4 = set((1,2,3))
s5 = set((1,1,2,2,3,3)) # 集合不會包含重複資料
print(s1)
print(s2)
print(s3)
print(s4) 
print(s5)
print(len(s5))
s10 = {1,3,6}
s10.add(20)
print(s10)
s10.remove(3)
print(s10)
# 集合 -----------------------------------------------
print('聯集 union ----------------------------------------')
set20={1,6,8,10,20}
set25={1,3,8,10}
# set20.union(set25)
print(set20|set25) # 不能有重複值
print('交集 intersection ---------------------------------')
set30={1,6,8,10,20}
set35={1,3,8,10}
print(set30&set35) # 有重複的留下來
print('差集 differemce ---------------------------------')
set40={1,6,8,10,20}
set45={1,3,8,10}
print(set40-set45) # 不重複的留下來
print('比較 ==: 或 !=: ---------------------------------')
set50={1,6,8,10,20}
set55={1,3,8,10}
print(set50!=set55) # 比較值，是否等於或不等於
# 詞典 -----------------------------------------------
dict1 = {'taipei':'101','paris':'tour Riffel','London':'big ben'}
dict1['Berlin'] = 'wall'
print(dict1['taipei'])
del dict1['taipei'] # 刪除某一個屬性
for key in dict1:     # 用迴圈倒出來，可設定倒屬性or值
    print('%s:%s' % (key,dict1[key]))
print(dict1.keys())   # 指顯示 屬性
print(dict1.values()) # 指顯示 值
print(dict1.items())  # 備註:前方會帶 dict_### 為Python的輸出規格
print(tuple(dict1.items())) #老師提供的輸出技巧:可移除掉前方贅字


