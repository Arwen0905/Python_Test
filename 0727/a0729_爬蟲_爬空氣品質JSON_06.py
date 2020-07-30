import pandas as pdA
import requests
import json
url = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json"
# pandas用法
# df = pd.read_json(url)
# df1 = pd.DataFrame(df[["County","SiteName","SiteId","PM2.5_AVG"]])
# df1.columns = {"城市","站台","站台ID","PM2.5值"}
# print(df1.head(50))

# requests用法
rq = requests.get(url).text
rs = json.loads(rq)
for i in rs:
    print(f'縣市:{i["County"]}, 站名:{i["SiteName"]},'\
          f' 站名id:{i["SiteId"]}, PM2.5值:{i["PM2.5"]}')
