import requests
from bs4 import BeautifulSoup
import time
import xlwt

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
url = "http://anqing.58.com/chuzu/pn"

def getPage(url):
    r = requests.get(url,headers = headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,"html.parser")
    names = soup.findAll("div",class_="des")
    addresses = soup.findAll("h2")
    moneys = soup.findAll("div",class_="money")
    accos = soup.findAll("p",class_="add")

    # data = []
    # for name,address,money in zip(names,addresses,moneys):
    #     data = {
    #         "name":name.find("a").get_text().strip(),
    #         "address":address.find("a").get("href"),
    #         "money":money.get_text().strip()
    #     }
    #     print(data)

    name = []
    address = []
    money = []
    acco = []

    for name2 in names:
        name1 = name2.find("a").get_text().strip()
        name.append(name1)
    for address2 in addresses:
        address1 = address2.find("a").get("href")
        address.append(address1)
    for money2 in moneys:
        money1 = money2.get_text().strip()
        money.append(money1)
    for acco2 in accos:
        acco.append(acco2.text.replace("|"," "))


    myExcel = xlwt.Workbook()
    sheet1 = myExcel.add_sheet(u"租房")
    sheet1.write(0, 0, "序号")
    sheet1.write(0, 1, "名称")
    sheet1.write(0, 2, "地址")
    sheet1.write(0, 3, "网址")
    sheet1.write(0, 4, "租金")

    for i in range(0, len(name)):
        sheet1.write(i + 1, 0, i + 1)
        sheet1.write(i + 1, 1, name[i])
        sheet1.write(i + 1, 2, acco[i])
        sheet1.write(i + 1, 3, address[i])
        sheet1.write(i + 1, 4, money[i])

    myExcel.save("C:/Users/hp/Desktop/58同城.xls")

for i in range(1,2):
    time.sleep(2)
    getPage(url+str(i))



