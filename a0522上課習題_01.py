#產生n個數字
#輸入產生數字的數量 及 欲查詢的最大值數字
import random
lst = []
i = 1
# while i <= 10:
#     s = eval(input('請輸入數字: '))
#     lst.append(s)
#     i+=1
# 自動產生-------------------------------------------
s = eval(input('輸入欲產生數字的數量: '))
count = 1
while count <= s:
    lst.append(random.randint(1, 100))
    count +=1
# -------------------------------------------    
# a = eval(input('輸入欲查詢的最大值數字: '))
a = 3 #欲取幾個數字 (預設3個)
# -------------------------------------------    
lst.sort()
print(lst,'<<< 串列10碼')
print('前',a,'個最大值數字',lst[-a-1:-1])

'''
老師解題參考
'''

def main():
    lst=[]
    # for i in range(5):
    #     num=eval(input('請輸入數值'))
    #     lst.append(num)
# 自動產生-------------------------------------------
    count = 1
    while count <= 10:
        lst.append(random.randint(1, 100))
        count +=1
# -------------------------------------------
    print(lst)
    print(compute(lst))
# 此函式接受一個串列 及一個a=帶數字(取得的次數)
def compute(lst,a=3):
    lst.sort()
    ans=[]
    for i in range(-1, -a-1, -1):
# (-1起始值, -1乘a等於{-值}後續的-1再補-1位, -1行進方式)
        ans.append(lst[i])
    return ans
main()
print(-1*5) # 驗證上述備註的算式：原來-數*正值會等於負值XD 缺乏常識

