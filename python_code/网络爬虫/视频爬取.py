import requests
import re
import urllib.request
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.3n6 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

def download(url):
    req = re.compile(r'srcUrl="(.*?)"')
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    for i in soup.findAll("div",class_='popularem-ath'):
        a = i.select('a')[0]
        id = a['href']
        title = a.find(class_='popularem-title').text
        new_url = 'http://www.pearvideo.com/{}'.format(id)
        res = requests.get(new_url, headers=headers, timeout=3).text
        get_video = re.findall(req, res)[0]
        print(get_video)
        print("正在下载",title)
        urllib.request.urlretrieve(get_video, "C:/Users/hp/Desktop/视频/{}.mp4".format(title))
        print("下载完成")


url = 'http://www.pearvideo.com/popular_4'
download(url)
