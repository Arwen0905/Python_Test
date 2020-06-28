lst = []
for i in range(12):
    n = int(input())
    lst.append(n)
    
ans=0
for index,i in enumerate(lst):
    print('%3d'%i,end='')
    if (index+1)%3==0:
        print()
    if index%2==0:
        ans+=i
print(ans)
