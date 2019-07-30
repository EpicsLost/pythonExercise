import requests
from bs4 import BeautifulSoup
import bs4
import xlwt
import pymysql

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillList(list,html):
    soup = BeautifulSoup(html,"html.parser")
    for i in soup.find("tbody").children:
        if isinstance(i,bs4.element.Tag):
            tds = i.find_all("td")  #tds = i("td")
            list.append([tds[0].string,tds[1].string,tds[3].string])

def printlist(list,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(("{0:^10}\t{1:{3}^6}\t{2:^16}").format("排名","学校名称","分数",chr(12288)))
    # a = ["排名","学校名称","分数"]
    # list.insert(0,a)
    for i in range(num):
        u = list[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def save_to_excel(list):
    myExcel = xlwt.Workbook()
    sheet1 = myExcel.add_sheet(u"中国大学排名")
    sheet1.write(0,0,"名次")
    sheet1.write(0,1,"学校名称")
    sheet1.write(0,2,"分数")
    for i in range(len(list)):
        sheet1.write(i + 1, 0, list[i][0])
        sheet1.write(i + 1, 1, list[i][1])
        sheet1.write(i + 1, 2, list[i][2])
    myExcel.save("中国大学排名.xls")

def mysql_create():
    mysql_host = ""
    mysql_db = "store"
    mysql_user = "root"
    mysql_password = "root"
    mysql_port = "3306"
    db = pymysql.connect(host = mysql_host, port = mysql_port, user = mysql_user, password = mysql_password, db = mysql_db,charset="utf-8")
    sql_create = "create table ChinaU(rank varchar(10),Uname varchar(20),grade varchar(20))"
    cursor = db.cursor()
    cursor.execute("drop table if exists ChinaU")
    cursor.execute(sql_create)
    db.close()

def IntoMysql(results):
    mysql_host = ""
    mysql_db = "store"
    mysql_user = "root"
    mysql_password = "root"
    mysql_port = "3306"
    db = pymysql.connect(host = mysql_host, port = mysql_port, user = mysql_user, password = mysql_password, db = mysql_db)
    cursor = db.cursor()
    for j in range(len(results)):
        try:
            sql = "insert into ChinaU(rank,Uname,grade) values ("
            for i in range(len(results[j])):
                sql = sql+"'"+results[j][i]+"',"
            sql = sql[:-1]+")"
            sql = sql.encode('utf-8')
            cursor.execute(sql)
            db.commit()
        except:pass
    db.close()


def main():
    list = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html = getHtml(url)
    mysql_create()
    fillList(list,html)
    #printlist(list,20)
    IntoMysql(list)
    save_to_excel(list)

main()