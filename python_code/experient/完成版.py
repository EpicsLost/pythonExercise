#coding=utf-8

import urllib
import re
import os
import threading
import time

exitFlag = 0


def Imagedownload(foldername,url,threadID):

    #创建文件路径G
    picpath = 'G:\\图片\\%s' %(foldername)
    #如果此路径不存在，创建一个文件路径
    if not os.path.exists(picpath):
        os.makedirs(picpath)

        currenturl = url           #构建url
        #print('Downloading pictures of the page %d...'% i)
        #异常处理.
        try:
            page = urllib.request.urlopen(currenturl)
            print(page)
        except urllib.URLError as e:
            #HTTPError异常处理
            if hasattr(e,'code'):
                print('The server cannot complete the request.')
                print('Errorcode:',e.code)
                input('please enter any key to exit...')
            #URLError异常处理
            elif hasattr(e,'reason'):
                print('The network unconnected.')
                print('Reason:',e.reason)
                input('please enter any key to exit...')
        else:
            print('''The network of Thread-'''+str(threadID)+''' has connected.\nThe server has worked.''')
        html = page.read()
        html = html.decode('utf-8')
        reg = r'src="(.+?\.jpg)" pic_ext'   #下载格式为图片
        imgre = re.compile(reg,re.I)             #编译正则表达式
        imglist = re.findall(imgre, html)   #匹配正则表达式，返回一个列表
        print(imglist)
        #回调函数，显示当前下载进度
        def  callbackfunc(blocknum, blocksize, totalsize):
            #blocknum: 已经下载的数据块
            #blocksize: 数据块的大小
            #totalsize: 远程文件的大小

            percent = 100.0 * blocknum * blocksize / totalsize
            if percent > 100:
                percent = 100
            print("%.2f%%"%percent)
        count = 0
        #在匹配后返回的列表中循环遍历，循环图片数
        for imgurl in imglist:
            count+=1                                    #计数
            targetimg = picpath+'\\%s.%s.jpg' %(threadID,count)#创建图片路径
            print('Downloading image to location: ' + targetimg + '\nurl=' + imgurl)
            threadpicNum[threadID] = count
            urllib.request.urlretrieve(imgurl,targetimg,callbackfunc) #下载图片后命名再保存到文件夹中

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.url = url       #申明URL为myThread类的私有成员变量并初始化
    def run(self):                   #重写run函数
        foldername=str(self.name)#创建文件夹名称
        Imagedownload(foldername, self.url, self.threadID)#下载
        print(self.name+' '+'Download has finished.\n')



if __name__ == '__main__':

    print('''                     *******************************************
                  **      Welcome to use Web Spider              **
                  **      Created on  '''+time.asctime( time.localtime(time.time()) )+'''   **
                  **      @author: suwenjun                      **
                     ********************************************   ''')
    #人工键入一个网站地址
    #mUrl=str(input('Please input a tieba website\n'))
    mUrl = "https://tieba.baidu.com/p/2460150866"
    #对键入的网站文本进行扫描

    #异常处理
    try:
        page = urllib.request.urlopen(mUrl)
    except urllib.error.URLError as e:
            #HTTPError异常处理
            if hasattr(e,'code'):
                print('The server cannot complete the request.')
                print('Errorcode:',e.code)
                input('please enter any key to exit...')
            #URLError异常处理
            elif hasattr(e,'reason'):
                print('The network unconnected.')
                print('Reason:',e.reason)
                input('please enter any key to exit...')
    else:
        print('''The network has connected.\nThe server has worked.''')
    html = page.read()
    html = html.decode('utf-8')
    addrre = re.compile(r'(<a.*?href=.*?>尾页</a>)',re.I)             #编译正则表达式(找到总共多少页码)
    addrlist = addrre.findall(html)   #匹配正则表达式，返回一个列表
    pattern = re.compile(r'<a.*?href=.*?pn=(\d+)">尾页</a>')
    for i in addrlist:
        # print(i)
        num = pattern.findall(i)
    else:
        threadNum = int(num.pop())
        print(threadNum)
        print('threadNum is confirmed !')


    threadpicNum = [0 for i in range(1,threadNum+1)]
    my_thread = [0 for i in range(1, threadNum+1)]
    for i in range(1, threadNum):
        my_thread[i] = myThread(i, 'Thread-'+str(i), i, mUrl+'/?pn='+str(i))
        my_thread[i].start()
    for i in range(1, threadNum):
        my_thread[i].join()

    print("Exiting Main Thread")
    #output=sys.stdout
    #outputfile=open('log.txt','w')
    #sys.stdout=outputfile
    for i in range(1,threadNum):
        print(mUrl+'/?pn='+str(i))
        print('Thread-'+str(i)+' has downloaded '+str(threadpicNum[i])+' pictures.\n')
    input('please enter any key to exit...')


#  http://tiebai.baidu.com/p/2460150866