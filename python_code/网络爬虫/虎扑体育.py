import requests
from bs4 import BeautifulSoup


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
url = "https://voice.hupu.com/nba"
r = requests.get(url,headers = headers)
r.encoding = r.apparent_encoding

soup = BeautifulSoup(r.text,"html.parser")
new_list = soup.find("div",class_="news-list")
news = new_list.find_all("li")
news_title = []
news_source = []

for i in news:
    try:
        title = i.find("h4").text.strip()
        source = i.find(class_="comeFrom").find("a").text.strip()
        news_title.append(title)
        news_source.append(source)
    except:
        continue
print("{:30}\t\t\t\t{:10}".format("新闻标题","新闻来源"))
for i in range(len(news_title)):
    print("{:30}\t\t{:10}".format(news_title[i],news_source[i]))









