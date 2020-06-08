import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x + 1
y2 = x**2

plt.plot(x,y1)
plt.show()
plt.plot(x,y2,color="#ff2244",linewidth="5")
plt.gca().set_facecolor("black")
plt.show()