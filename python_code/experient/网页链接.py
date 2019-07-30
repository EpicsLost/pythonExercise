import requests
import re
import threading
from requests.exceptions import RequestException
from queue import Queue
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        return None
    except RequestException:
        return None

#获取该链接下的每个网页链接,返回一个列表
def getUrl(html):
    soup = BeautifulSoup(html.text,"html.parser")
    html = soup.body
    pattern = re.compile(r'<a.*?href="(.*?)".*?</a>')
    hreflist = re.findall(pattern,str(html))
    return hreflist

#获取每张图片的链接,返回一个列表
def getImg(html):
    pattern = re.compile(r'src="(.*?\.jpg)"')
    imglist = re.findall(pattern,html.text)
    return imglist

class MyThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
        #self.threadname = threadname

    def run(self):
        while(True):
            href = self.queue.get()
            #print(href)
            if href[0:4] == "http":
                #获取到当期那页面中每一个网页链接的信息
                html = getHtml(href)
                if html is not None:
                    save_pic(html)
            if self.queue.empty():
                break



def save_pic(html):
    global count
    #根据每个网页获取每个.jpg文件
    img = getImg(html)
    if len(img)!=0:
        print(img)
    # for i in range(len(img)):
    #     h = getHtml(img[i])
    #     with open ("pic/%s.jpg"%count,"wb") as f:
    #         f.write(h.content)
    #     count = count+1

def main():
    global count
    url = "http://tieba.baidu.com/p/2460150866"
    target = "http://tieba.baidu.com"
    html = getHtml(url)
    hreflist = getUrl(html)
    queue = Queue()
    threads = []
    count = 0

    #下载当前页面中的所有图片
    #save_pic(html)

    for i in range(len(hreflist)):
        if hreflist[i][:1] == "/":
            hreflist[i] = target+hreflist[i]

    #将当前页面所有链接存放到队列中
    for i in range(len(hreflist)):
        queue.put(hreflist[i])


    thread = MyThread(queue)
    thread.start()
    thread.join()
    threads.append(thread)

    # for thread in threads:
    #     thread.join()

if __name__ == "__main__":
    main()
    print("Done!")