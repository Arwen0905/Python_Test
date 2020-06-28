def compute(a,b):
    ans=0
    for i in range(a,b+1):
        ans+=i
    return ans
a = eval(input())
b = eval(input())
print(compute(a,b))
