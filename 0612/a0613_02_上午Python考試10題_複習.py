# (1):輸入國文、英文、數學三科成績後，計算總分及平均成績
lst = []
while True:
    c = eval(input('請輸入國文成績: '))
    lst.append(c)
    e = eval(input('請輸入英文成績: '))
    lst.append(e)
    n = eval(input('請輸入數學成績: '))
    lst.append(n)
    print('總分為:%d，平均成績為%d'%(sum(lst),sum(lst)/3))
    break

# (2):輸入上底、下底與高的數值後，計算梯形的面積
# (梯形面積公式:(上底+下底)*高/2)
up = eval(input('輸入上底的數值: '))
down = eval(input('輸入下底的數值: '))
high = eval(input('輸入高的數值: '))
print('梯形面積公式:%.2f'%((up+down)*high/2))

# (3):百貨公司週年慶，公司決定消費超過2000元的顧客就打75折增加買氣。
# 請幫公司寫出一程式，輸入顧客總金額後，計算顧客實際需付的金額。
price = eval(input('輸入消費金額: '))
if price >= 2000:
    print('折扣後的金額為: %d元'%(price * 0.75))
else:
    print('消費金額為: %d元'%price)

# (4):請輸入月份，判斷是什麼季節?
# (春天:3~5月；夏天:6~8月；秋天:9~11月；冬天:12-2月)
month = eval(input('輸入月份: '))
if 3 <=month<=5:
    print('春天')
elif 6<=month<=8:
    print('夏天')
elif 9<=month<=11:
    print('秋天')
elif 12<=month<=2:
    print('冬天')

# (5):請設計一程式，計算級數1+2+4+7+11...+106的過程和結果。
ans = 1
for i in range(1,107):
    print(ans)
    ans += i
 
# (6):請設計一程式，讓使用者輸入英文句子，
# 程式會以空格來切割句子。切成多個單字並輸出
en = str(input('輸入英文句子，間隔以空格表示: '))
en = en.split(' ')
for i in en:
    print('切割的單字為: ',i)

# (7):請設計一程式，讓使用者輸入姓名與電話，，當要結束輸入通訊資料時，
# 可以輸入「finish」結束。接著可以查詢通訊錄姓名，程式會回應其通訊電話
# ，若沒有會回復「不在通訊中」。
user = {}
while True:
    name = str(input('請輸入姓名: '))
    if name == 'finish':
        break
    user.setdefault(name)
    phone = int(input('請輸入電話: '))
    if phone == 'finish':
        break
    user[name] = phone
print(user)
ans = str(input('查詢通訊錄姓名: '))
if ans in user:
    print(user.get(ans))
else:
    print('不在通訊中')


# (8):請撰寫一程式，呼叫一個自訂函式f()，
# 計算某一整數的n次方。例如「請輸入要計算的整數:x」；
# 「請輸入要計算的次方數:y」，輸出「x的y次方 結果是:」
def f():
    x = eval(input('請輸入要計算的整數: '))
    y = eval(input('請輸入要計算的次方數: '))
    print('%d的%d次方 結果是:%d '%(x,y,x**y))
f()





