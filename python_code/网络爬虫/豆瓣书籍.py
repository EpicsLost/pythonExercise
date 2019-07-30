import requests
import xlwt
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

def get_page(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
    }

    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_page(html,list):
    soup = BeautifulSoup(html,"html.parser")
    div = soup.find("div",class_="mod book-list")
    for i in div.find_all("dd"):
        title = i.find("a",class_="title").get_text()
        someinfo = i.find("div",class_="desc").get_text().strip()
        info = someinfo.split("/")
        price = info[-1]
        writer = info[0:-3]
        publish = info[-3]
        rate = i.find("div",class_="rating").find("span",class_="rating_nums").get_text()
        if float(rate) < 9:
            list.append([title,writer,publish,rate,price])
    return list

def save_excel(list):
    myExcel = xlwt.Workbook()
    sheet1 = myExcel.add_sheet("豆瓣读书")
    sheet1.write(0,0,"书名")
    sheet1.write(0,1,"作者")
    sheet1.write(0,2,"出版社")
    sheet1.write(0,3,"评分")
    sheet1.write(0,4,"价格")
    for i in range(len(list)):
        sheet1.write(i + 1, 0, list[i][0])
        sheet1.write(i + 1, 1, list[i][1][0])
        sheet1.write(i + 1, 2, list[i][2])
        sheet1.write(i + 1, 3, list[i][3])
        sheet1.write(i + 1, 4, list[i][4])
    myExcel.save("C:/Users/hp/Desktop/豆瓣小说.xls")

def main():
    url = "https://www.douban.com/tag/小说/book?start="
    list = []
    for i in range(0,2):
        url = url+str(i)
        i = i+15
        html = get_page(url)
        result = parse_page(html,list)
    save_excel(list)

if __name__ == "__main__":
    main()
