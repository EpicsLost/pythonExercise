import requests
from bs4 import BeautifulSoup
import sys

class downloader():
    def __init__(self):
        self.server = "http://www.biqugew.com"
        self.target = "http://www.biqugew.com/book/9/"
        self.name = []
        self.urls = []
        self.nums = 0

    def get_downloader_url(self):
        req = requests.get(url = self.target)
        req.encoding = "gbk"
        html = req.text
        bf = BeautifulSoup(html,"html.parser")
        div = bf.findAll("div",id = "list")
        a_bf = BeautifulSoup(str(div),"html.parser")
        a = a_bf.findAll("a")
        self.nums = len(a)
        for i in a:
            self.name.append(i.string)
            self.urls.append(self.server+i.get("href"))

    def get_content(self,target):
        req = requests.get(url = target)
        req.encoding = "gbk"
        bf = BeautifulSoup(req.text,"html.parser")
        texts = bf.findAll("div",id = "content")
        texts = texts[0].text.replace("\xa0*4","")
        return texts

    def writer(self,name,path,text):
        write_flag = True
        with open (path,"w",encoding="utf-8") as f:
            f.write(name+"\n")
            f.writelines(text)
            f.write("\n")

if __name__  == "__main__":
    dl = downloader()
    dl.get_downloader_url()
    print("《斗破苍穹》开始下载:")
    count = 0
    for i in range(dl.nums):
        dl.writer(dl.name[i],"C:/Users/hp/Desktop/斗破苍穹/{a}.txt".format(a = count),dl.get_content(dl.urls[i]))
        count += 1
        sys.stdout.write("已下载：%.3f%%"%(float(i/dl.nums*100))+"\r")
        sys.stdout.flush()
    print("下载完成！")