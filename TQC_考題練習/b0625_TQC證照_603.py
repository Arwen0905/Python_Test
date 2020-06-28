lst=[]
for i in range(10):
    n = eval(input())
    lst.append(n)
lst.sort()
print(lst[-1],lst[-2],lst[-3])