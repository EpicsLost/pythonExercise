import requests
from bs4 import BeautifulSoup
import urllib.request

url = "http://player.youku.com/embed/XMTgyNzU5ODg5Ng"

data = requests.get(url)
print(type(data.content))
with open("C:/Users/hp/Desktop/视频/1.mp4","w") as f:
    f.write(data.text)


