# TODO
x,y = eval(input())
# x,y=12,8
def compute(x,y):
    k=1
    while k<x and k<y:
        if x%k==0 and y%k==0:
            gcd = k
        k+=1
    return gcd
print(compute(x,y))