# TODO
col = row = 3
lst = []
max_num = min_num = 0
max_index = min_index = [0,0]
for i in range(col):
    lst.append([])
    for j in range(row):
        n = eval(input())
        lst[i].append(n)
        if n > max_num:
            max_num = n
            max_index = [i,j]
        elif n < min_num:
            min_num = n
            min_index = [i,j]
            
print('Index of the largest number %d is: (%d, %d)'%(max_num,max_index[0],max_index[1]))
print('Index of the smallest number %d is: (%d, %d)'%(min_num,min_index[0],min_index[1]))

"""
Index of the largest number _ is: (_, _)
Index of the smallest number _ is: (_, _)
"""