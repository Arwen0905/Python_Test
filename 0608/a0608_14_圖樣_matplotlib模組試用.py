import matplotlib.pyplot as plt
x = [1,2,4,6,8,1,2,9,3]
y = [5,7,2,3,1,4,6,5,8]
# 數據龐大的情況，需要用迴圈設定大小，對效能較好
plt.scatter(x,y,s=[500 for i in range(len(x))],c='r',alpha="0.5"\
            ,marker=r"$\star$")
plt.title("Scatter simple")
plt.xlabel("x axes")
plt.ylabel("y axes")
plt.show()
