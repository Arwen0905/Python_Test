import requests, bs4
url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
rq = requests.get(url)
soup = bs4.BeautifulSoup(rq.text,"lxml")

rs = soup.select('ul.release_list')
# rs = soup.select('div.release_info')
# print(rs[0].select('a'))
print(rs[0].select('.release_movie_time'))
# for v,i in enumerate(rs):
    # print(i.select('.release_movie_time')[v].text)
    # print(i.select('a')[0].text)
    # print(i.select('.release_movie_time')[0].text)
    
