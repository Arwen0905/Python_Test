a = int(input())
b = int(input())
count = sum = 0
if a<=b:
    for i in range(a,b+1):
       if  i%4==0 or i%9==0:
           print('%-4d'%i,end='')
           sum+=i
           count+=1
           if count%10==0:
               print()
print()
print(count)
print(sum)
