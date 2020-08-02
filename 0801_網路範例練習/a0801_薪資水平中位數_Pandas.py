import requests
import pandas as pd

url = "https://mops.twse.com.tw/mops/web/ajax_t100sb15"
payload = {
    "encodeURIComponent": "1",
    "step": "1",
    "firstin": "1",
    "TYPEK": "sii",
    "RYEAR": "108",
    }
rq = requests.post(url,data=payload).text
df = pd.read_html(rq)
# print(df[0].columns)
df = df[0].iloc[:,[0,1,2,5,6,7]]
# print(df[0].head())
df.columns = ["產業類別","公司代號","公司名稱","108年平均數",
              "107年平均數","108年中位數"]
df = df.sort_values('108年中位數',ascending=False)
# print(df.median())
print(df.iloc[:,[3,4,5]].median())
