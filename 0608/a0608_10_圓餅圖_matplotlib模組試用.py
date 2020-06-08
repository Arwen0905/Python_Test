import matplotlib.pyplot as plt
labels = "A","B","C","D","E","F"
size = [33,52,12,17,62,48]
                                    # 輸出格式
plt.pie(size,labels = labels, autopct="%1.1f%%")
plt.axis("equal")
plt.show()
