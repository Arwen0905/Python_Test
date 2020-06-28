print("Enter matrix 1:")
lst=[[0 for i in range(2)]for k in range(2)]
for i in range(2):
    for j in range(2):
        lst[i][j]=eval(input("[%d, %d]: " % (i+1, j+1)))    
        
print("Enter matrix 2:")
lst2=[[0 for i in range(2)]for k in range(2)]
for i in range(2):
    for j in range(2):
        lst2[i][j]=eval(input("[%d, %d]: " % (i+1, j+1)))    
  
print("Matrix 1:")
lst3=[[0 for i in range(2)]for k in range(2)]
for i in range(2):
    for j in range(2):
        print(lst[i][j],end=' ')
    print()
    
print("Matrix 2:")
for i in range(2):
    for j in range(2):
        print(lst2[i][j],end=' ')
    print()

print("Sum of 2 matrices:")
for i in range(2):
    for j in range(2):
        lst3[i][j] = lst[i][j] + lst2[i][j]
        print(lst3[i][j],end=' ')
    print()
