import requests
from bs4 import BeautifulSoup as soup
url = "https://google.com"
url2 = "https://gamewith.tw/monsterstrike/article/show/86304"
re = requests.get(url2)
re.encoding = "utf-8"
rs = soup(re.text,"html.parser")
print(rs.prettify())


