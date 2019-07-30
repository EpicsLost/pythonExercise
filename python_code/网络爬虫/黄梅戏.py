import requests
import json
import os
import threading

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
}

url = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%BB%84%E6%A2%85%E6%88%8F&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E9%BB%84%E6%A2%85%E6%88%8F&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&pn=30&rn=30&gsm=1e&1538184843430="
response = requests.get(url)
data = response.text
info = json.loads(data)
# print(type(data))
for i in range(len(info.get('data'))):
    each = info.get('data')[i]
    if each is not None:
        print(each.get('middleURL'))

print(info.get('queryExt').encode("utf-8"))

