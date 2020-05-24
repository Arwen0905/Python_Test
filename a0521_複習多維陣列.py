import pymysql
db = pymysql.connect(
    "localhost","root",
    "123456",
    "data_base_one",
    charset="utf8"
    )
sql = 'SELECT * FROM table_two'
cursor = db.cursor()
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    print(i[0],i[1],i[3])
db.commit()
db.close()

# 1 -------------------------------------------------------
import random
lotto = []  # 樂透碼
randNum = [] # 隨機碼
n = 1 # 判斷次數
while n<=6:
    randNum = random.randint(1, 49) # 創建一個隨機碼
    print(randNum, '<<< 外部裝入樂透碼')
    if randNum not in lotto: # 條件需不存在lotto裡，才允許填入
        lotto.append(randNum) # 確認填入
        print(lotto) # 印出當前樂透碼
        n+=1 # 次數+1
lotto.sort()
print('\n本期樂透:\n%s' % lotto)
print()
# 2 -------------------------------------------------------
lotto = [] # 樂透碼
checkNum = [] # 不重複碼
for i in range(1,50): # 進入迴圈，給予1-49次
    checkNum.append(0) # 填入49次，數值都為:0
print(checkNum)
count = 1
while count <= 6:
    randNum = random.randint(1, 49) # 隨機索引一個號碼(1~49)
    if checkNum[randNum] == 0:
        lotto.append(randNum)
        print(lotto,' <<< 當前樂透碼')
        checkNum[randNum] = 1
        print(checkNum)
        count += 1
print('樂透號碼:')
lotto.sort()
for i in lotto:
    print(i,end=' ')
print()


