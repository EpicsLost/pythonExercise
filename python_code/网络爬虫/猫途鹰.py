import requests
from bs4 import BeautifulSoup

urls = "https://www.tripadvisor.cn/Attractions-g294212-Activities-oa30-Beijing.html#FILTERED_LIST"#format(str(i) for i in range(30,930,30))]
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
def getPage(url):
    r = requests.get(url,headers = headers)
    # soup = BeautifulSoup(r.text,"lxml")
    # titles = soup.select('div.list-title > a[target="_blank"]')
    # imgs = soup.select("img[width=180]")
    # cates = soup.select('span[class="matchedTag.noTagImg"]')
    soup = BeautifulSoup(r.text,"html.parser")
    titles = soup.findAll("div",class_="listing_title")
    imgs = soup.findAll("div",class_="photo_booking non_generic")
    data = {}
    for title,img in zip(titles,imgs):
        data = {
            "title":title.find("a").get_text(),
            "img"  :img.find("img").get("src"),
        }
        print(data)

getPage(urls)