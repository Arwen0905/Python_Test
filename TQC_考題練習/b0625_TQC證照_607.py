title = ['1st','2nd','3rd']
lst = [[0 for i in range(5)]for i in range(3)]
for i in range(3):
    print('The %s student:'%(title[i]))
    for j in range(5):
        lst[i][j]=eval(input())

for i in range(3):
    print('Student %d'%(i+1))
    print('#Sum %d'%sum(lst[i]))
    print('#Average %.2f'%(sum(lst[i])/5))

    
# lst1,lst2,lst3=[],[],[]
# n = ["1st","2nd","3rd"]
# print('The %s student:'%n[0])
# for i in range(5):
#     lst1.append(eval(input()))
# print('The %s student:'%n[1])
# for i in range(5):
#     lst2.append(eval(input()))
# print('The %s student:'%n[2])
# for i in range(5):
#     lst3.append(eval(input()))
# print('Student %d'%1)
# print('#Sum %d'%sum(lst1))
# print('#Average %.2f'%(sum(lst1)/5))
# print('Student %d'%2)
# print('#Sum %d'%sum(lst2))
# print('#Average %.2f'%(sum(lst2)/5))
# print('Student %d'%3)
# print('#Sum %d'%sum(lst3))
# print('#Average %.2f'%(sum(lst3)/5))





  