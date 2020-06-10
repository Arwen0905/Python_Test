import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5*np.pi, 1000)
y1 = np.sin(x)
y2 = np.sin(2*x)

plt.plot(x, y1, label = "$y=sin(x)$",\
         color="#ff2244",linestyle="-",linewidth=3)
plt.plot(x, y2, label = "$y=sin(2*x)$",linestyle="-",linewidth=5)
plt.legend(loc=3)
plt.show()
