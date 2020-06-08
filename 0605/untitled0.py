import pandas as pd
datas = [[65,92,78,83,70],[90,72,76,93,56],[81,85,91,89,77],[79,53,47,94,80]]
indexs = ["李大年","王大同","黃美娟","陳美玲"]
columns = ["國文","數學","英文","自然","社會"]
df = pd.DataFrame(datas,columns=columns,index=indexs)
print(df)
df.to_csv('pdout.csv',encoding='utf-8-sig')