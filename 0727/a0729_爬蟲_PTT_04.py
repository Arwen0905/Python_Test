import requests, bs4
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text,'lxml')

# 自己寫 ==========================================================================

pttdivs = objSoup.select('div.bbs-screen > .r-ent')
# print(pttdivs)
for i in pttdivs:
    # print(i)
    print(i.select('.title')[0].text.strip())
    print(i.select('a')[0].get('href'))
    print(i.select('.author')[0].text)


# ==========================================================================
print('='*50)

# articles = []
# pttdivs = objSoup.find_all('div','r-ent')

# for p in pttdivs:
#     if p.find('a'):
#         title = p.find('a').text
#         author = p.find('div','author').text
#         href = p.find('a')['href']
#         articles.append({'title':title,
#                           'author':author,
#                           'href':href,
#                           })

# print('本頁的文章數量 = ', len(articles))
# count = 0
# for article in articles:
#     count += 1
#     print('文章編號: ',count)
#     print('文章標題: ',article['title'])
#     print('文章作者: ',article['author'])
#     print('文章連結: ',article['href'],'\n')
