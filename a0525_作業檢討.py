import random
lista = []
count = 1
while count <= 100:
    num = random.randint(1, 100)
    if num not in lista:
        lista.append(num)
        count+=1
# print(lista)
# print(len(lista))
lista.sort()
for j in range(101): #10? >101
    if j % 10 == 0:
        print('%4d'% lista[j-1]) #lista? >lista[j-1]
    else:
        print('%4d'% lista[j-1],end=' ')


