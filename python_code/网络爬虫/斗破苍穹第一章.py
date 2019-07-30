import requests
from bs4 import BeautifulSoup

url = "http://www.biqugew.com/book/9/4446.html"
req = requests.get(url)
req.encoding = "gbk"
html = req.text
bf = BeautifulSoup(html,"html.parser")
text = bf.findAll("div",id="content")
result = text[0].text.replace("\xa0"*4,"")

with open("cha1.txt","w",encoding="utf-8") as f:
    f.write(result)