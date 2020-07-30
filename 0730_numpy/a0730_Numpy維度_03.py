import numpy as np
a = np.arange(6).reshape(3,2)
print(a)
print("="*50)

b = np.array([a,a])
print(b)

# print(b.shape)

print(np.random.rand())
print(np.random.randint(10))
print(np.random.rand(2,3))
print(np.random.randint(10,size=(2,3)))


print("="*50)

# 機器學習(?
# (1)建立20個(x,y)組合之座標點
x = np.random.rand(20)*8-4
print(x)
y = np.sin(x)+np.random.rand(20)*0.2
print(y)
# (2)以一次方項開始測試
# f(x) = w,x+w0
# =>使用 np.polyfit()函式
#   格式:polyfit(x,y,次方數)
#   傳回係數 w,w0(以一次方項為例)


oma = np.polyfit(x,y,5)
# 以一元五次多項式
# 可使20資料點撮合於取線上，完成迴歸分析
f = np.poly1d(oma)
import matplotlib.pyplot as plt
plt.xlabel("x")
plt.ylabel("y")
plt.title("傻眼")
plt.grid()
plt.scatter(x,y,marker="x",c="red")
xx = np.linspace(-4, 4, 100)
# -4 ~ 4 之間產生100個值(x座標)
plt.plot(xx,f(xx),color='green')
plt.show()



