import random
def lotto():
    lotto =[]
    count = 1
    while count <= 6:
        n = random.randint(1, 49)
        if n not in lotto:
            lotto.append(n)
            count+=1
    lotto.sort(reverse=True) # !新技巧!
    # print(lotto,'樂透號碼產生')
    return lotto
def mainRow():
    lotto5=[]
    for row in range(5):
        lotto5.append(lotto())        
    print(lotto5)
def main():
    for i in range(5):
        print('樂透產生器',lotto())
mainRow()
main()

'''
老師解題
'''
# def mainNum():
#     for i in range(5):
#         print(lotto(),'老師範例')
# mainNum()