from bs4 import BeautifulSoup
import requests
rq = requests.get('https://tw.yahoo.com')
soup = BeautifulSoup(rq.text,'html.parser')
titles = soup.find_all('a',class_='story-title')
for row in titles:
    print(row.text)
    # print(row.get('href'))
