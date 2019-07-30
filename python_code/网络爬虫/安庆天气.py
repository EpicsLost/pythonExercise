from lxml import etree
import requests

url = "http://www.weather.com.cn/weather/101220601.shtml"
response = requests.get(url)
response.encoding = "utf-8"
html = etree.HTML(response.text)

print("安庆明天的天气：")
date = html.xpath('//*[@id="7d"]/ul/li[2]/h1/text()')[0]
wea  = html.xpath('//*[@id="7d"]/ul/li[2]/p[1]/text()')[0]
tem1 = html.xpath('//*[@id="7d"]/ul/li[2]/p[2]/span/text()')[0]
tem2 = html.xpath('//*[@id="7d"]/ul/li[2]/p[2]/i/text()')[0]
tem =tem1+'/'+tem2
print(date,wea,tem)

