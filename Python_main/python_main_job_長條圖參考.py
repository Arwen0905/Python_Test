import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# labels = ['G1', 'G2', 'G3', 'G4', 'G5'] #標題
df1_col_name = ["台北", "新北", "台中", "彰化", "高雄"]
df1_Taiwan_ans = [2.34, 3.4, 3.8, 3.5, 2.7]

# women_means = [25, 32, 34, 20, 25]
x = np.arange(len(df1_col_name))  # the label locations
print(x/0.35)
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(df1_col_name,x- width/2,  width, label='Men')
rects2 = ax.bar(df1_col_name,x+ width/2,  width, label='Men')
# rects1 = ax.bar(x - width/2, men_means, width, label='Men')
# rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
# autolabel(rects2)

# fig.tight_layout()

# plt.show()