from pathlib import Path
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import re
import threading

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
}

def get_page(url):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response
        return None
    except RequestException:
        return None

def create_dir(name):
    #根据传入的目录名创建一个目录
    directory = Path(name)
    if not directory.exists():
        directory.mkdir()
    return directory

path = create_dir("C:/Users/hp/Desktop/tieba")

def get_page_index():
    url = "http://tieba.baidu.com/p/2460150866"
    html = get_page(url)
    soup = BeautifulSoup(html.text,"lxml")
    pattern1 = re.compile(r'(<a.*?href=.*?>尾页</a>)',re.I)
    addrlist = pattern1.findall(html.text)
    pattern2 = re.compile(r'\d+')
    for i in addrlist:
        num = pattern2.findall(i)
    Num = int(num.pop())
    return Num

def download(Num):
    for i in range(Num):
        file_path = create_dir(path / str(i + 1))
        url = "http://tieba.baidu.com/p/2460150866?pn="+str(i+1)
        html = get_page(url)
        pattern = re.compile(r'src="(.*?\.jpg)" pic_ext')
        addr = re.findall(pattern,html.text)
        for i in range(len(addr)):
            html = get_page(addr[i])
            pic_path = "{0}/{1}.{2}".format(file_path,str(i+1),"jpg")
            with open (pic_path,"wb") as f:
                f.write(html.content)

class Mythread(threading.Thread):
    def __init__(self,Num):
        threading.Thread.__init__(self)
        self.Num = Num
    def run(self):
        download(self.Num)

if __name__ == "__main__":
    num = get_page_index()
    download(num)



