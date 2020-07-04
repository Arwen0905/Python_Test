import pandas as pd
import matplotlib.pyplot as plt
cities = {'population':[1000,850,800,1500,600,800],
          'town':['New York','Chicago','Bangkok','Tokyo',
                  'Singapore','Hongkong']}
tw = pd.DataFrame(cities,columns=['population'],index=cities['town'])
print(tw) # 檢視

# 畫圖
tw.plot(title="Population in the world",kind='bar')
plt.xlabel('City')
plt.ylabel('Population')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()