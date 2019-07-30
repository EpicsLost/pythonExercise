import re
import requests
from bs4 import BeautifulSoup


def getHtml(url,code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""
def getStockList(list,stocklisturl):
    html = getHtml(stocklisturl,"gb2312")
    soup = BeautifulSoup(html,"html.parser")
    a = soup.findAll("a")
    for i in a:
        try:
            href = i.attrs["href"]
            list.append(re.findall(r"[s][hz]\d{6}",href))
        except:
            continue

def getStockInfo(list,stockinfourl,fpath):
    count = 0
    for stock in list:
        html = getHtml(stockinfourl+str(stock)+".html")
        try:
            if html == "":
                continue
            infodic = {}
            soup = BeautifulSoup(html, "html.parser")
            div = soup.findAll("div", class_="stock-bets")
            name = div.findAll("div",class_="bets-name")[0]
            infodic.update({"股票名称":name.text.split()[0]})

            keylist = soup.findAll("dt")
            valuelist = soup.findAll("dd")
            for i in range(len(keylist)):
                key = keylist[i].text
                value = valuelist[i].text
                infodic[key] = value
            with open(fpath,"a",encoding = "utf-8") as f:
                f.write(str(infodic) + "\n")
                count = count+1
                print("\r当前速度：{:.2f}%".format(count*100/len(list)),end = "")
        except:
            count = count + 1
            print("\r当前速度：{:.2f}%".format(count * 100 / len(list)), end="")
            continue
def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    file_path = "C:/User/hp/Desktop/stock.txt"
    list = []
    getStockList(list,stock_list_url)
    getStockInfo(list,stock_info_url,file_path)

main()