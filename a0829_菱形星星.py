
k=eval(input("輸入數字長度"))

for i in range(0,k):
    for j in range(k-1,i,-1):
        print("  ",end='')
    for s in range(0,i+1):
        print(" *",end='')
    for s in range(0,i):
        print(" *",end='')
    print()
    
for i in range(1,k):
    for s in range(0,i):
        print("  ",end='')
    for j in range(i,k-1):
        print(" *",end='')
    for j in range(0,k-i):
        print(" *",end='')
    print()
