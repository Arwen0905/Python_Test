import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5*np.pi, 0.1)
y = np.sin(x*2)
# plt.plot(list_x1, list_y1,color="#ffff55",linewidth="5",\
         # linestyle="-.",label=list_x2)
plt.title("sine wave form")
plt.plot(x,y,color="red",linestyle="solid",linewidth=5)
plt.gca().set_facecolor("black")
plt.show()
