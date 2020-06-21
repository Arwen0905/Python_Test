# 第一類
# 1=====================================================
# lst = []
# for i in range(4):
#     n = eval(input())
#     lst.append(n)
# print('|%5d%5d|'%(lst[0],lst[1]))
# print('|%5d%5d|'%(lst[2],lst[3]))
# print('|%-5d%-5d|'%(lst[0],lst[1]))
# print('|%-5d%-5d|'%(lst[2],lst[3]))
# 2=====================================================
# lst = []
# for i in range(4):
#     n = eval(input())
#     lst.append(n)
# print('|%7.2f %7.2f|'%(lst[0],lst[1]))
# print('|%7.2f %7.2f|'%(lst[2],lst[3]))
# print('|%-7.2f %-7.2f|'%(lst[0],lst[1]))
# print('|%-7.2f %-7.2f|'%(lst[2],lst[3]))
# 3=====================================================
# lst=[]
# for i in range(4):
#     s = str(input())
#     lst.append(s)
# print('|%10s %10s|'%(lst[0],lst[1]))
# print('|%10s %10s|'%(lst[2],lst[3]))
# print('|%-10s %-10s|'%(lst[0],lst[1]))
# print('|%-10s %-10s|'%(lst[2],lst[3]))
# 4=====================================================
# import math
# r = eval(input())
# m = r*2*math.pi
# l = r**2*math.pi
# print('Radius = %.2f'%r)
# print('Perimeter = %.2f'%m)
# print('Area = %.2f'%l)
# 5=====================================================
# l = eval(input())
# w = eval(input())
# print('Height = %.2f'%l)
# print('Width = %.2f'%w)
# print('Perimeter = %.2f'%(w*2+l*2))
# print('Area = %.2f'%(w*l))
# 6=====================================================
# x = eval(input())
# y = eval(input())
# z = eval(input())
# x = x*60 # x分鐘 * 60 = 取得秒數
# ans = (z/1.6)/(x+y)*60*60
# print('Speed = %.1f'%ans)
# 7====================================================
# lst=[]
# for i in range(5):
#     n = eval(input())
#     lst.append(n)
# print(*map(str,lst))
# print('Sum = %.1f' %sum(lst))
# print('Average = %.1f' %(sum(lst)/len(lst)))
# 8=====================================================
# x1,y1,x2,y2 =eval(input()),eval(input()),eval(input()),eval(input())
# ans = ((x1-x2)**2) + ((y1-y2)**2)
# print('( %s , %s )'%(x1,y1))
# print('( %s , %s )'%(x2,y2))
# print('Distance = %.4f'%(ans**0.5))
# 9=====================================================
# import math
# s=eval(input())
# Area = (5*s**2)/(4*math.tan(math.pi/5))
# print('Area = %.4f'%Area)
# 10=====================================================
# import math
# n,s=eval(input()),eval(input())
# Area = (n*s**2)/(4*math.tan(math.pi/n))
# print('Area = %.4f'%Area)
# =====================================================
# 第二類
# 1=====================================================
# n = eval(input())
# if n%2 == 0:
#     print('%d is an even number.'%n)
# elif n%2 != 0:
#     print('%d is not an even number.'%n)
# 2=====================================================
# n = eval(input())
# if n%3==0 and n%5!=0:
#     print('%d is a multiple of 3.'%n)
# elif n%5==0 and n%3!=0:
#     print('%d is a multiple of 5.'%n)
# elif n%5==0 and n%3==0:
#     print('%d is a multiple of 3 and 5.'%n)
# elif n%5!=0 and n%3!=0:
#     print('%d is not a multiple of 3 or 5.'%n)
# 3=============================================
# year = eval(input())
# if year%4 == 0 and year%100 != 0:
#     print('%d is a leap year.'%year)
# elif year%400 == 0 or year%1000 ==0:
#     print('%d is a leap year.'%year)
# else:
#      print('%d is not a leap year.'%year)
# 4=============================================
# a,b = eval(input()),eval(input())
# x = str(input())
# if x == '+':
#     print(a+b)
# elif x == '-':
#     print(a-b)
# elif x == '*':
#     print(a*b)
# elif x == '/':
#     print(a/b)
# elif x == '//':
#     print(a//b)
# elif x == '%':
#     print(a%b)
# 5=============================================
# x = input()
# if x.encode('utf8').isalpha():
#     print('%s is an alphabet.'%x)
# elif x.strip('-').isdigit():
#     print('%s is a number.'%x)
# else:
#     print('%s is a symbol.'%x)
# 6=============================================
# x = eval(input())
# if 100 >= x >=80:
#     print('A')
# elif 79 >= x >=70:
#     print('B')
# elif 69 >= x >=60:
#     print('C')
# elif x < 59:
#     print('F')
# else:
#     print('error')
# 7=============================================
# n = eval(input())
# if n >= 8000:
#     print(n*0.95)
# elif n >= 18000:
#     print(n*0.9)
# elif n >= 28000:
#     print(n*0.8)
# elif n >= 38000:
#     print(n*0.7)
# 8=============================================
# n = eval(input())
# if 0<= n <=9:
#     print(n)
# elif n == 10:
#     print('A')
# elif n == 11:
#     print('B')
# elif n == 12:
#     print('C')
# elif n == 13:
#     print('D')
# elif n == 14:
#     print('E')
# elif n == 15:
#     print('F')    
# 9=============================================
# x,y=eval(input()),eval(input())
# ans = (((x*1)-(5))**2 + ((y*1)-(6))**2)**0.5
# if ans <= 15:
#     print('Inside')
# elif ans > 15:
#     print('Outside')
# 10=============================================
# n1,n2,n3=eval(input()),eval(input()),eval(input())
# if n1+n2 >n3 and n2+n3 >n1 and n3+n1 >n2:
#     print(n1+n2+n3)
# else:
#     print('Invalid')
# =============================================
# 第三類
# 1=============================================
# a,b = eval(input()),eval(input())
# total = 0
# for i in range(a,b+1):
#     total += i
# print(total)
# 2=============================================
# total=0
# a,b=eval(input()),eval(input())
# for i in range(a,b+1):
#     if i%2==0:
#         total+=i
# print(total)
# 3=============================================
# n = eval(input())
# for i in range(1,n+1):
#     for k in range(1,i+1):
#         print('%4d'%(i*k),end='')
#     print()
# 4=============================================
# total=0
# a=eval(input())
# for i in range(1,a+1):
#     if i%5==0:
#        total+=i
# print(total)
# 5=============================================
# n = eval(input())
# while n!=0:
#     print(n%10,end='')
#     n = n//10
# 6=============================================
# n = eval(input())
# result=1
# for i in range(1,n+1):
#     result*=i
# print(result)
# 7=============================================
# n = eval(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print('%-2d* %-2d= %-4d'%(j,i,(i*j)),end='')
#     print()
# 8=============================================
# total = eval(input())
# for i in range(total):
#     ans = 0
#     n = input()
#     lst = list(n)
#     for i in lst:
#         ans+= eval(i)
#     print('Sum of all digits of %s is %d'%(n,ans))
# 9=============================================
# amount,rate,moths = eval(input()),eval(input()),eval(input())
# print('%s \t  %s' % ('Month', 'Amount'))
# for i in range(1,moths+1):
#     amount += amount*rate/1200
#     print('%3d \t %.2f' % (i, amount))
# 10=============================================
# n = eval(input())
# ans = 0
# for i in range(2,n+1):
#     ans += 1/((i-1)**0.5+i**0.5)
# print('%.4f'%ans)
# 第四類
# 2=============================================
# lst=[]
# while True:
#     n = eval(input())
#     if n == 9999:
#         break
#     lst.append(n)
# print(min(lst))
# 4=============================================
# n = input()
# lst = list(n)
# lst.reverse()
# for i in lst:
#     print(i,end='')
# 6=============================================
# while True:
#     cm = eval(input())
#     if cm == -9999:
#         break
#     kg = eval(input())
#     if kg == -9999:
#         break
#     ans = kg/(cm/100)**2
#     # ans = kg / (cm/100 * cm/100)
#     if ans < 18.5:
#         print('BMI: %.2f'%ans)
#         print('State: under weight')
#     elif 18.5<= ans <25:
#         print('BMI: %.2f'%ans)
#         print('State: normal')
#     elif 25<= ans <30:
#         print('BMI: %.2f'%ans)
#         print('State: over weight')
#     elif ans >= 30:
#         print('BMI: %.2f'%ans)
#         print('State: fat')
# =============================================
# 第五類
# 2=============================================
# x,y=eval(input()),eval(input())
# compute=lambda x,y:x*y
# print(compute(x,y))
# 4=============================================
# a,b=eval(input()),eval(input())
# compute=lambda a,b:a**b
# print(compute(a,b))
# 10=============================================

# =============================================
# 第六類
# 2=============================================
# ans=0
# for i in range(5):
#     n = input().upper()
#     if n == 'J':
#         ans+=11
#     elif n == 'Q':
#         ans+=12
#     elif n == 'K':
#         ans+=13
#     elif n == 'A':
#         ans+=1
#     else:
#         ans+=eval(n)
# print(ans)
# 4=============================================
# lst=[]
# tem=[0]*10
# for i in range(10):
#     n = eval(input())
#     lst.append(n)
#     tem[lst.index(n)] += 1
# print(lst[tem.index(max(tem))])
# print(max(tem))
# =============================================
# 第七類
# 2=============================================
# tup1,tup2=tuple(),tuple()
# print('Create tuple1:')
# while True:
#     n = eval(input())
#     if n == -9999:
#         break
#     tup1+=n,
# print('Create tuple2:')
# while True:
#     n = eval(input())
#     if n == -9999:
#         break
#     tup2+=n,
# print('Combined tuple before sorting:',(tup1+tup2))
# print('Combined list after sorting:',sorted(list(tup1+tup2)))
# 4=============================================
# set1 = set()
# while True:
#     n = eval(input())
#     if n == -9999:
#         break
#     set1.add(n)
# print('Length:',len(set1))
# print('Max:',max(set1))
# print('Min:',min(set1))
# print('Sum:',sum(set1))
# =============================================
