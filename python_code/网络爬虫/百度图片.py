import os
import urllib.request
import threading
import re


# 获取本地的要搜索关键字的名单
def getNameList(filename):
    # 没加encoding='utf-8'导致UnicodeDecodeError: 'gbk' codec can't decode byte 0x8f in position 14: illegal multibyte sequence
    file = open(filename, encoding='utf-8')
    keywordlist = file.readlines()
    for i in range(len(keywordlist)):
        keywordlist[i] = keywordlist[i].replace('\n', '').strip()
    print(keywordlist)
    return keywordlist


def getHtml(url):
    # 没加.decode('utf-8')导致TypeError: cannot use a string pattern on a bytes-like object
    outhtml = urllib.request.urlopen(url).read().decode('utf-8')
    return outhtml


# pn是页码
def getUrl(url, word, pn):
    # urlopen不能处理中文字符，因此需要将中文转码
    word = urllib.parse.quote(word)
    surl = url.format(word=word, pn=pn)
    # print(surl)
    return surl

def getUrlsFromHtml(html):
    reg = '"thumbURL":"(.*?)"'
    # imgre是(.*?)匹配到的东西，此处是图片链接
    imgre = re.compile(reg, re.S)
    imglist = re.findall(reg, html)
    # print(imglist)
    return imglist


def downLoadImg(urls, path, keyword, downloadnum, picnumPerKeyword):
    index = downloadnum
    for url in urls:
        print("下载：", url)
        try:
            filename = os.path.join(path, keyword + str(index) + ".jpg")
            urllib.request.urlretrieve(url, filename)
            index += 1
            if (index >= picnumPerKeyword):
                break;
        except Exception as e:
            print("There is an Exception!")
            index -= 1
    return index


def imgDwonloadThread(url, keyword, picnumPerKeyword, savepatn):
    pn = 0
    downloadnum = 0
    print('下载：', keyword)
    while downloadnum < picnumPerKeyword:
        newurl = getUrl(url, keyword, pn)
        html = getHtml(newurl)
        # 得到图片的链接
        urls = getUrlsFromHtml(html)
        downloadnum = downLoadImg(urls, savepatn, keyword, downloadnum, picnumPerKeyword)
        pn += 30

def main():
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1514256634296_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word={word}&cg=girl&rn=60&pn={pn}'
    keywordfile = "./file"

    if not os.path.exists('pythonDownLoad'):
        os.mkdir('pythonDownLoad')
    savepatn = "pythonDownLoad/"
    #keywordlist = getNameList(keywordfile)
    keyword = "黄梅戏"
    #下载图片数
    picnumPerKeyword = 200
    #for keyword in keywordlist:
        # 新开一个线程
    try:
        thread = threading.Thread(target=imgDwonloadThread, args=(url, keyword, picnumPerKeyword, savepatn))
        thread.start()
    except:
        print("创建新线程失败！")


main()
