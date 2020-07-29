import pandas as pd
url = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json"
df = pd.read_json(url)
df1 = pd.DataFrame(df[["County","SiteName","SiteId","PM2.5_AVG"]])
df1.columns = {"城市","站台","站台ID","PM2.5值"}
print(df1.head(50))

