import pandas as pd
name = ['阿冬','小芳']
city = ['台北市','彰化市']
phone = ['0988-999-777','0966-666-888']
ran = range(2020,2021)
name = pd.Series(name,index=ran)
city = pd.Series(city,index=ran)
phone = pd.Series(phone,index=ran)
name.name,city.name,phone.name = "姓名","城市","電話"
user = pd.concat([name,city,phone],axis=1) # 要裝串列才行
# title = ['姓名','城市','電話']
# user.columns = title
print(user)
