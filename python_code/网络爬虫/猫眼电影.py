import requests
from requests.exceptions import RequestException
import re
import json
import time
# 多线程,一秒完成数据的爬取
from multiprocessing import Pool

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'
                         '.*?<p.*?"name"><.*?title="(.*?)"'
                         '.*?"star">(.*?)</p>'
                         '.*?"releasetime">(.*?)</p>'
                         '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'
                         , re.S)

    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'title': item[1],
            'actor': item[2].strip()[3:],
            'time':  item[3].strip()[5:],
            'score': item[4] + item[5]

        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
     # for i in range(10):
     #     time.sleep(2)
     #     main(i*10)
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])