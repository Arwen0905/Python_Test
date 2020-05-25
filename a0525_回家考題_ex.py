#01
# 以 while 迴圈撰寫九九乘法表。
y=1
while y<=9:
    x = 1
    while x<=y:
        print('%d+%d=%d'%(x,y,x*y),'\t',sep='',end='')
        x += 1
    print()
    y+=1
print()

#02
# 請撰寫一程式，
# 讓使用者輸入一個正整數(<100)，
# 然後以三角形的方式依序輸出此數的階乘結果。
# 提示：輸出欄寬為 4，且須靠左對齊。

# num = eval(input('請輸入一個小於100的正整數: '))
num = 5
for i in range(0,num):
    for j in range(0,i+1):
        print(' * ', end='')
    print()
    
#03
# 請撰寫一程式，
# 讓使用者輸入兩個正整數 a、b (a<b)，
# 利用迴圈計算從 a 開始的偶數連加到 b 的總和。
# 例如：輸入 a = 1、b = 100，則輸出結果為 2550。
ab = 0
switch = True
while switch:
    switch = False
    # a = int(float(input('請輸入一個起始正整數: ')))
    # b = int(float(input('請輸入一個終止正整數: ')))
    a,b = 1,100
    if a<b:
        for i in range(a,b,2):
            i = i+1 % 3
            ab += i
        print('[',a,',',b,']',ab)
        print()
        switch = False
    elif a==b:
        print('錯誤! 起始值%2d等於終止值%2d，運算不成立'%(a,b))
        switch = True
    elif a>b:
        print('錯誤! 終止值%2d小於起使值%2d，運算不成立'%(b,a))
        switch = True
    else:
        print('錯誤! 輸入格式錯誤，運算不成立'%(b,a))
        switch = True

#04
# 請撰寫一程式，
# 讓使用者輸入一個正整數(<100)，
# 印出以下的左上三角形。
# 提示：輸出欄寬為 4，且須靠左對齊。
# num = int(float(input('請輸入一個小於100的正整數: ')))
num = 5
for i in range(num,0,-1):
    for j in range(i,0,-1):
        print(' * ',end='')
    print()

#05
# 請撰寫一程式，
# 由使用者輸入一數字，
# 然後印出 1 到此數字的階乘。

import math
# num = int(float(input('請輸入階乘數字')))
num = 10
print(num)
for i in range(1,num+1):
    factorial = math.factorial(i)
    print('%d! ='%i,factorial)
