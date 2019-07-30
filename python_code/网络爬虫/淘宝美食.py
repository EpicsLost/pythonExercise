from pathlib import Path

import requests
from requests import RequestException
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
}

def search():
    try:
        browser.get("https://www.taobao.com")
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#q")))
        submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button")))
        input.send_keys("美食")
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.total")))
        get_product()
        return total.text
    except TimeoutException:
        return search()

def next_page(page_number):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.form > input")))
        submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.active > span"),str(page_number)))
        #next = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.next > a")))
        get_product()
    except TimeoutException:
        return next_page(page_number)

def get_product():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-itemlist .items .item")))
    html = browser.page_source
    doc = pq(html)
    items = doc("#mainsrp-itemlist .items .item").items()
    for item in items:
        product = {
            "image":item.find(".pic .img").attr("src"),
            "price":item.find(".price").text(),
            "title":item.find(".title").text()
        }
        print(product)
        # save_dir = create_dir("C:/Users/hp/Desktop/美食")
        # download(save_dir,item.find(".title").text(),item.find(".pic .img").attr("src"))

def create_dir(name):
    directory = Path(name)
    if not directory.exists():
        directory.mkdir()
    return directory

def save(dir,title,content):
    path = "{0}/{1}.{2}".format(dir,title,"jpg")
    with open (path,"wb") as f:
        f.write(content)

def download(dir,title,url):
    print("正在下载：",url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save(dir,title,response.content)
        return None
    except RequestException:
        return None



def main():
    total = search()
    total = int(re.compile("(\d+)").search(total).group(0))
    for i in range(1):
        next_page(i)

main()