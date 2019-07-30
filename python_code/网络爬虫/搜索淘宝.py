import requests
#import re
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 "}
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
        return r.text
    except:
        return ""

def parsepage(list1,list2,html):
    # try:
    #     plt = re.findall(r'\"price\"\:\"[\d\.]*\"',html)
    #     tlt = re.findall(r'\"title\"\:\".*?\"',html)
    #     for i in range(len(plt)):
    #         price = eval(plt[i].split(":")[1])
    #         title = eval(tlt[i].split(":")[1])
    #         list.append([price,title])
    # except:
    #     print("")
    try:
        soup = BeautifulSoup(html,"html.parser")
        span1_bf = soup.findAll("span")
        for i in span1_bf:
            title = i.get("title")
            list1.append(title)
        for j in soup.findAll("strong"):
            price = j.string
            list2.append(price)
    except:
        print("")


def printlist(list1,list2):
    tplt = "{:4}\t{:8}\t{:4}"
    print(tplt.format("序号","价格","商品名称"))
    for i in range(len(list2)):
        print(tplt.format(i,str(list2[i]),str(list1[i])))

def main():
    infolist1 = []
    infolist2 = []
    depth = 2
    start_url = "http://uland.taobao.com/sem/tbsearch?&keyword=书包&page="
    for i in range(depth):
        try:
            url = start_url + str(i+1)
            html = getHtml(url)
            parsepage(infolist1,infolist2,html)
        except:
            continue
    printlist(infolist1,infolist2)

main()