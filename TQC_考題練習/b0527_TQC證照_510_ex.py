def compute(x):
    n1,n2 = 0,1
    print(n1,end=' ')
    if x > 0:
        for i in range(1,x):
            print(n2,end=' ')
            n3 = n1 + n2
            n1 = n2
            n2 = n3
x = int(input())
compute(x)
