import requests
from bs4 import BeautifulSoup
import re
import xlwt

def getHtml(url):
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        r = requests.get(url,headers = headers)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsepage(title,year,html):
    soup = BeautifulSoup(html,"html.parser")
    div = soup.find_all("div",class_ = "item")
    for i in div:
        try:
            title1 = i.find("span",class_="title").text
            year_info = i.find("div",class_="bd").find("p").text
            year1 = "".join(re.findall("\d",year_info))
            title.append(title1)
            year.append(year1)
        except:
            continue

def printpage(title,year):
    print("{0:^6}\t{1:{3}^20}\t{2:^10}".format("序号", "电影名称", "年份", chr(12288)))
    for i in range(len(title)):
        print("{0:^6}\t{1:{3}^20}\t{2:^10}".format(i+1,title[i],year[i],chr(12288)))

def save_excel(title,year):
    myExcel = xlwt.Workbook()
    sheet1 = myExcel.add_sheet(u"top250 Film")
    sheet1.write(0, 0, "序号")
    sheet1.write(0, 1, "电影名称")
    sheet1.write(0, 2, "上映时间")
    for i in range(0, len(title)):
        sheet1.write(i + 1, 0, i + 1)
        sheet1.write(i + 1, 1, title[i])
        sheet1.write(i + 1, 2, year[i])
    myExcel.save("./top250.xls")

def main():
    url = "https://movie.douban.com/top250?start="
    title = []
    year = []
    for i in range(0,10):
        try:
            html = getHtml(url+str(25*i))
            parsepage(title,year,html)
        except:
            continue
    #printpage(title,year)
    save_excel(title,year)

main()