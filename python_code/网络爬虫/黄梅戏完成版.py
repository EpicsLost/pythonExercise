import os
import urllib.request
import threading
import re
import requests

def getHtml(url):
    html = requests.get(url).text
    return html

# pn是页码
def getUrl(url, word, pn):
    # urlopen不能处理中文字符，因此需要将中文转码
    word = urllib.parse.quote(word)
    surl = url.format(word=word, pn=pn)
    return surl

#获取图片链接
def getUrlsFromHtml(html):
    reg = '"thumbURL":"(.*?)"'
    imglist = re.findall(reg, html)
    # print(imglist)
    return imglist

def downLoadImg(urls, path, keyword, downloadnum, picnum):
    index = downloadnum
    for url in urls:
        print("下载：", url)
        try:
            filename = os.path.join(path, keyword + str(index) + ".jpg")
            urllib.request.urlretrieve(url, filename)
            index += 1
            if (index >= picnum):
                break;
        except Exception as e:
            print("Error!")
            index -= 1
    return index


def imgDwonloadThread(url, keyword, picnum, savepatn):
    pn = 0
    downloadnum = 0
    print('下载：', keyword)
    while downloadnum < picnum:
        newurl = getUrl(url, keyword, pn)
        html = getHtml(newurl)
        # 得到图片的链接
        urls = getUrlsFromHtml(html)
        downloadnum = downLoadImg(urls, savepatn, keyword, downloadnum, picnum)
        pn += 30

def main():
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1514256634296_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word={word}&cg=girl&rn=60&pn={pn}'
    if not os.path.exists('黄梅戏图片'):
        os.mkdir('黄梅戏图片')
    savepatn = "黄梅戏图片/"
    keyword = "黄梅戏"

    #下载图片数
    picnum = 200
    try:
        thread = threading.Thread(target=imgDwonloadThread, args=(url, keyword, picnum, savepatn))
        thread.start()
    except:
        print("创建新线程失败！")

if __name__ == '__main__':
    main()
