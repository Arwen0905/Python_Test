import matplotlib.pyplot as plt
x = ['bk','sw','ph','rd','gu']
a = [8, 7, 1, 6, 5]
b = [12, 2, 9, 5, 3]
plt.bar(x, a, label="a",align="edge",color="#ffff55",width=0.3)
plt.bar(x, b, label="a",align="edge",color="#ff2244",width=-0.3)
plt.gca().set_facecolor("black")

