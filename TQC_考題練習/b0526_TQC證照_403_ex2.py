a = int(input())
b = int(input())
list1=[]
count = 0
sum = 0
while a<=b:
    for i in range(a,b+1):
       if  i%4==0 and i%9==0:
           list1.append(i)
           count+=1
           sum+=i
    print('%-4s'%list1)

