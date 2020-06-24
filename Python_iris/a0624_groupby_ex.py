import pandas as pd
df = pd.DataFrame(data={"books":["b1","b1","b1","b2","b2","b2"],
				"price":[12,12,12,15,15,17]})
print(df)
print()
print(df.groupby("books",as_index=True).sum())
print()
print(df.groupby("books",as_index=False).sum())
