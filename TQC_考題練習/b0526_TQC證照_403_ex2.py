a = int(input())
b = int(input())
list1=[]
count = sum = 0
if a<=b:
    for i in range(a,b+1):
       if  i%4==0 or i%9==0:
           list1.append(i)
           sum+=i
    for i in list1:
        print('%-4s'%i,end='')
        count+=1
        if count%10==0:
            print()
print()
print(count)
print(sum)
