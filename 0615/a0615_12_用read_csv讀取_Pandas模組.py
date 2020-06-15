import pandas as pd
course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
x = pd.read_csv('out_a.csv',index_col=0)
y = pd.read_csv('out_b.csv',names=course)
print(x)
print(y)
