from bs4 import BeautifulSoup
import requests
from time import sleep

google_url = 'https://google.com'
my_params = {"q":"東踏取蜜"}
rq = requests.get('https://www.google.com.tw/search', params=my_params)
sleep(1)
if rq.status_code == requests.codes.ok:
    # soup = BeautifulSoup(rq.text,'html.parser')
    # soup_html = soup.prettify()
    # print(soup_html)
    
    soup = BeautifulSoup(rq.text,'html.parser')
    # rs = soup.select('h3')
    # rs = soup.findAll('h3')
    rs = soup.findAll('h3 > a[href^="/url"]')
    # print(rs)
    for row in rs:
        print(row.text)
    # sleep(1)
    # for i in rs:
    #     print(i.text)
    #     print(i.get('href'))
