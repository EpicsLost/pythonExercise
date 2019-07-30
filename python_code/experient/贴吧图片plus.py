import urllib
import requests
from requests.exceptions import RequestException
import re
import threading
from queue import Queue

#获取页面的内容
def getHtml(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        return None
    except RequestException:
        return None

#获取每张图片的链接
def getUrl(html):
    pattern = re.compile(r'src="(.*?\.jpg)" pic_ext')
    imglist = re.findall(pattern,html)
    return imglist

class MyThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        global count
        while(True):
            imgurl = self.queue.get()
            print(imgurl)
            path = "pic/%s.jpg"%count
            print(path)
            html = getHtml(imgurl)
            with open (path,"wb") as f:
                f.write(html.content)
            count += 1
            if self.queue.empty():
                break

def main():
    global count
    url = "http://tieba.baidu.com/p/2460150866"
    html = getHtml(url).text
    imglist = getUrl(html)
    print(imglist)
    threads = []
    count = 0
    queue = Queue()

    #将所有任务加入队列
    for i in range(len(imglist)):
        queue.put(imglist[i])

    #多线程爬取图片
    for i in range(4):
        thread = MyThread(queue)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
    print("Done!")