import requests
from bs4 import BeautifulSoup

server = "http://www.biqugew.com"
url = "http://www.biqugew.com/book/9/"
req = requests.get(url)
req.encoding = req.apparent_encoding
bf = BeautifulSoup(req.text,"html.parser")
div = bf.findAll("div",id = "list")
a_bf = BeautifulSoup(str(div[0]),"html.parser")
a = a_bf.findAll("a")
for i in a:
    print(i.string,server+i.get("href"))

