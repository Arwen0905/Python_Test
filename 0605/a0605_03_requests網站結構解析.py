import requests
payload = {'key1':'value1','key2':'value2'}
html = requests.get("http://httpbin.org/get",params=payload)
# ※測試結果 用data替代params後即能隱藏掉標頭資訊
# html = requests.get("http://httpbin.org/get",data=payload)
print(html.url,'<< get')
html = requests.post("http://httpbin.org/post",data=payload)
print(html.text,'<< text')
print(html.url,'<< post')
