from _md5 import md5
from pathlib import Path

import requests
from urllib.parse import urlencode
import re
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import json

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
}

def get_page_index(offset,keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab'
    }

    url = "https://www.toutiao.com/search_content/?"+urlencode(data)
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求索引页出错")
        return None

def parse_page_index(html):
    data = json.loads(html)
    #print(type(data))
    if data and "data" in data.keys():
        for item in data.get("data"):
            if item.get("article_url") == None:
                continue
            else:
                yield item.get("article_url")

def get_detailed(url):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求详情出错！")
        return None

def parse_detailed(html,url):
    soup = BeautifulSoup(html,"lxml")
    title = soup.select("title")[0].get_text()
    pattern = re.compile('.*?gallery: JSON.parse\(\"(.*?)\"\).*?',re.S)
    result = re.search(pattern,html)
    if result:
        data = json.loads(result.group(1).replace('\\',''))
        if data and "sub_images" in data.keys():
            sub_images = data.get("sub_images")
            images = [item.get("url") for item in sub_images]

            save_dir = create_dir("C:/Users/hp/Desktop/图片/")
            save_dir = create_dir(save_dir/title)
            for i in images:
                download(save_dir, i)

            return {
                "title":title,
                "url"  :url,
                "image":images
            }

def create_dir(name):
    directory = Path(name)
    if not directory.exists():
        directory.mkdir()
    return directory

def save_images(save_dir,content):
    file_path = "{0}/{1}.{2}".format(save_dir, md5(content).hexdigest(),"jpg")
    with open (file_path, "wb") as f:
        f.write(content)

def download(save_dir,url):
    print("正在下载:",url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_images(save_dir,response.content)
        return None
    except RequestException:
        print("请求图片错误！")
        return None

def main():
    save_dir = "C:/Users/hp/Desktop/街拍"
    html = get_page_index(0,"街拍")
    for url in parse_page_index(html):
        html1 = get_detailed(url)
        if html1:
            parse_detailed(html1,url)


if __name__ ==  '__main__':
    main()
