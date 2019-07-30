import requests
from bs4 import BeautifulSoup

url = "https://www.tripadvisor.cn/Attractions-g294212-Activities-oa30-Beijing.html#FILTERED_LIST"
headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"}

r = requests.get(url,headers = headers)
soup = BeautifulSoup(r.text,"lxml")# div.container.containerLLR > div.title.titleLLR > div

titles = soup.select("div.container.containerLLR > div.title.titleLLR > div")#a1979768 > div.thumb.thumbLLR.soThumb
for i in titles:
    print(i.get_text())
