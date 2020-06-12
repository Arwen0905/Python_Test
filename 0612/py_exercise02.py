# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:28:49 2020

@author: ASUS
"""

# 1. 分數計算
chi= eval(input("請輸入國文分數:"))
eng= eval(input("請輸入英文分數:"))
mat= eval(input("請輸入數學分數:"))

sum=(chi+eng+mat)
avg=sum/3

print()
print("總分為%.1f, 平均分數為%.1f" % (sum, avg))

# 2. 梯型面積

upper= eval(input("請輸入梯型上底長度:"))
lower= eval(input("請輸入梯型下底長度:"))
heigh= eval(input("請輸入梯型高度:"))
area= (upper+lower)*heigh/2
print()
print("梯型面積為 %d" % area)

# 3. 百貨公司周年慶

price= eval(input("請輸入商品總金額:"))
if price >= 2000:
    print("應付金額為 %d" % round(price*0.75))
else:
    print("應付金額為 %d" % price)

# 4. 季節判斷

month= int(input("請輸入月份:"))
if month==3 or month==4 or month==5:
    print("春天")
elif month==6 or month==7 or month==8:
    print("夏天")
elif month==9 or month==10 or month==11:
    print("秋天")
elif month==12 or month==1 or month==2:
    print("冬天")
else:
    print("無此月份")

# 5. 計算遞加級數

def main():
    i=1
    sum=0
    for i in range(1,107,i):
        sum+=i
    print(sum)
main()


# 6. 輸入句子切割成單字

def singleword():
    sentence=str(input("請輸入英文句子:"))
    word=sentence.split()
    for i in word:
        print(i)
singleword()


# 7. 通訊錄

def phonebook():
    namelst=[]
    phonelst=[]
    while True:
        name = (input("請輸入姓名:"))
        if name == "finish":
            break
        phone = (input("請輸入電話:"))
        if phone == "finish":
            break
        namelst.append(name) 
        phonelst.append(phone)
    
    searchname=(input("請輸入欲查找知姓名:"))
    if searchname in namelst:
        print()
        print("電話號碼為:",phonelst[namelst.index(searchname)])
    else:
        print("不在通訊錄中")

phonebook()

# 8. 次方計算

def f():
    print("請輸入要計算的整數:x")
    x=int(input())
    print("請輸入要計算的次方:y")
    y=int(input())
    result=x**y
    print()
    print("x的y次方為%d" % result)

f()








