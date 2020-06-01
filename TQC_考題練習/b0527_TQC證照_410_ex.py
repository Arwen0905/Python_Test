# TODO
n = 5
# n = int(input())
for i in range(1,n+1): # 1-(5)
    for j in range(n,i,-1): # (5)-0
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()
    