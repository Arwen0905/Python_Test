import requests
from bs4 import BeautifulSoup
from time import sleep
google_url = 'https://www.google.com.tw/search'
my_params = {'q': '寒流'}
r = requests.get(google_url, params = my_params)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    html_prettify = soup.prettify()
    # print(html_prettify)
    items = soup.select('div.g > h3.r > a[href^="/url"]')
    sleep(3)
    for i in items:
        print("標題：" + i.text)
        print("網址：" + i.get('href'))