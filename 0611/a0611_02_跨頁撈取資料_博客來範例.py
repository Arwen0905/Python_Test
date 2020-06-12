import requests
from lxml import etree
from time import sleep

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

title = []
price = []
link = []

def search (url):
    print(url)
    res = requests.get(url,headers=headers)
    content = res.content.decode()
    html = etree.HTML(content)
    # title.extend(html.xpath('//*[@id="searchlist"]/ul/li/h3/a/@title'))
    # print(title)
    # link.extend(html.xpath('//*[@id="searchlist"]/ul/li/h3/a/@href'))
    # price.extend(html.xpath('//*[@id="searchlist"]/ul/li/span[@class="price"]/strong[not(contains(text(),"折"))]/b/text()'))
    
    # next_page = html.xpath('//a[@class="nxt"]/@href')
    # if len(next_page)==0 or next_page[0]=="#" :
    #     return "finish"
    # else:
    #     sleep(.5)
    #     return search("http:"+next_page[0])
        
def getAllBooks(keyword):
    search(f'https://search.books.com.tw/search/query?fclick=0&key={keyword}&cat=all')


getAllBooks('python')