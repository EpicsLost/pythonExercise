import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import os
import threading

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
}
def getPage(start):

    #https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
    url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={0}&limit=20".format(start)
    return_data = requests.get(url, verify = False)
    #print(return_data.text)
    response = return_data.text

    data = json.loads(response)#type:list

    for i in range(len(data)):
        global count
        if not os.path.exists('pics/'):
            os.mkdir('pics/')
        path = "pics/{0}.{1}".format(count, 'jpg')
        count += 1
        res = requests.get(data[i].get('cover_url'))
        print("正在下载:",count,data[i].get('cover_url'))
        with open (path,"wb") as f:
            f.write(res.content)

        #print(data[i].get('cover_url'))

def main():
    global count
    count = 1
    while True:
        i = 0
        start = i*20
        getPage(start)
        i+=1

if __name__ == '__main__':
    myThread = threading.Thread(main())
    myThread.start()