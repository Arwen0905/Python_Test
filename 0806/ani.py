import requests

url = 'https://ani.gamer.com.tw/'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

rq = requests.get(url , headers = headers)
print(rq.text)

# r = requests.get(url , cookies = {'over18': '1'})
# if r.status_code == requests.codes.ok:
    