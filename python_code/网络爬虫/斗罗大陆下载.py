import requests
from bs4 import BeautifulSoup
from lxml import etree
import os

def getPage(url):
    response = requests.get(url)
    response.encoding="gbk"
    return response.text

def get_menu(html):
    page = etree.HTML(html)
    hrefs = []
    names = []
    for each in page.xpath('//div[@id="main"]//ul//li'):
        href = each.xpath('./a/@href')
        name = each.xpath('./a/text()')
        hrefs.append(href)
        names.append(name)
    return hrefs,names

def get_content(html):
    soup = BeautifulSoup(html,"html.parser")
    content = soup.findAll("div",id = "htmlContent")
    content = content[0].text.replace("\xa0*4","")
    return content


if __name__ == '__main__':
    url = "http://www.metege.com/0_485/"
    html = getPage(url)
    each_urls = []
    print(get_menu(html)[1])
    # for i in get_menu(html):
    #     each_url = url+i[0]
    #     each_urls.append(each_url)
    # each = each_urls[0]
    # content_html = getPage(each)
    # print(get_content(content_html))
