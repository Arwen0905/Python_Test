from bs4 import BeautifulSoup
import requests
from time import sleep
rq = requests.session()
google_url = 'https://google.com'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac os x 10_12_3)'\
            'Applewebkit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

my_params = {"q":"東踏取蜜"}
rq.post('https://www.google.com.tw/search', headers=headers, params=my_params)
sleep(1)
rq = requests.get('https://www.google.com.tw/search', headers=headers, params=my_params)
sleep(1)
if rq.status_code == requests.codes.ok:
    soup = BeautifulSoup(rq.text,'html.parser')
    rs = soup.select('div.g > h3.r > a[href^="/url"]')
    for i in rs:
        print(i.text)
        print(i.get('href'))