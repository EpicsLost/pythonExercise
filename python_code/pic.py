import urllib.request
from bs4 import BeautifulSoup

def getAllImage(url):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html.read())
    imgResult = soup.find_all("img")

    count = 0
    for images in imgResult:
        count += 1
        link = images.get("src")
        imageName = count
        filesavepath = "C:/Users/hp/Desktop/picture/"
        urllib.request.urlretrieve(link,filesavepath)
        print(filesavepath)
if __name__ == "__main__":
    cate = "壁纸"
    n = 10
    getAllImage('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))