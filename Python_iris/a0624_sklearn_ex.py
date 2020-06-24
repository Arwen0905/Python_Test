from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()
# 兩列、四欄
fig = plt.figure(figsize=(3,3))
# 調整紙圖形的參數: 左右上下，包括位置跟間距
fig.subplots_adjust(left=0,right=1,bottom=0,top=1,hspace=0.05,wspace=0.05)

for i in range(9):
    # 加入到紙圖形。兩列四欄的位置上，第三個參數為[你要寫的位置]:0+1
    ax=fig.add_subplot(3,3,i+1,xticks=[],yticks=[]) #xticks=[空值]為坐標軸關閉
    # 秀出 digits的 imgs
    ax.imshow(digits.images[i],cmap=plt.cm.binary)
    # 加入文字，digits的target就是目標值[i]
    ax.text(0,7, str(digits.target[i]))
print(digits)

# lst=[]
# max_search,min_search=[],[]
# max=0
# min=100
# for i in range(3):
#     lst.append([])
#     for j in range(3):
#         n = eval(input())
#         lst[i].append(n)
#         if n>max:
#             max=n
#             max_search=[i,j]
#         elif n<min:
#             min=n
#             min_search=[i,j]
# print(lst)
# print(min,"( ",min_search[0],",",min_search[1]," )")
# print(max,"( ",max_search[0],",",max_search[1]," )")
        