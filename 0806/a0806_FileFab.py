import requests
from bs4 import BeautifulSoup
import random

url = "http://ip.filefab.com/index.php"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
rq = requests.get(url, headers=headers)
# print(rq.text)

soup = BeautifulSoup(rq.text,"lxml")
rs = soup.select("#ipd > span")[0].text
# print(rs)

# 代理伺服器查詢: http://ip.filefab.com/index.php
proxy_ips = ['192.168.56.1:8085','114.32.56.96:3333']
ip = random.choice(proxy_ips)
print('Use',ip)
resp = requests.get(url,proxies={'http':'http://'+ip})
soup = BeautifulSoup(resp.text,"htm5lbli")
print(soup.find('h1',id='ipd').text.strip())

