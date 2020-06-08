from matplotlib import pyplot as plt
import random
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
x,y,x2,y2,x3,y3=[],[],[],[],[],[]
for i in range(3):
    x.append(random.randint(1, 30))
    y.append(random.randint(1, 30))
    x2.append(random.randint(1, 30))
    y2.append(random.randint(1, 30))
    x3.append(random.randint(1, 30))
    y3.append(random.randint(1, 30))

plt.bar(x,y,align="center",color="#ffff55")
plt.bar(x2,y2,align="center",color="#55ffff")
plt.bar(x3,y3,align="center",color="pink")
plt.title("Bar graph",color="blue")
plt.ylabel("Y axis",color="#ff2244")
plt.xlabel("X axis",color="#ff2244")
plt.gca().set_facecolor("black")
plt.show()

