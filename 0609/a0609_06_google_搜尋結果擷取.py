from bs4 import BeautifulSoup
import requests
from time import sleep

google_url = 'https://google.com'
my_params = {"q":"東踏取蜜"}
rq = requests.get('https://www.google.com.tw/search', params=my_params)
sleep(1)
if rq.status_code == requests.codes.ok:
    soup = BeautifulSoup(rq.text,'html.parser')
    rs = soup.select('div.g > h3.r > a[href^="/url"]')
    for i in rs:
        print(i.text)
        print(i.get('href'))
