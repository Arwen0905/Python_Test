import random
lista = []
count = 1
while count <= 100:
    num = random.randint(1, 100)
    if num not in lista:
        lista.append(num)
        count+=1
lista.sort()
print(lista)
# print(len(lista))
# for j in range(1,101): # 較直觀的使用方式
for j in range(1,101): # 老師範例
    if j % 10 == 0:
        # print('%4d'% j) # 這裡換行
        print('%4d'% lista[j-1]) # 換行
    else:
        # print('%4d'% j,end=' ') # end黏住，不換行
        print('%4d'% lista[j-1],end=' ') # 不換行

################### for的range(單數)會從0開始 ####################
################### 因為迴圈1開始，[索引]要回去撈0的數字 ##########
