import requests
from bs4 import BeautifulSoup

def get(i):
    url = "http://210.45.175.14/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    dt = soup.find("img",title = "看不清，换一张")
    print(dt.get("src"))
    s = dt.get('src')
    re = requests.get("http://210.45.175.14/"+s)
    with open ("C:/Users/hp/Desktop/验证码/"+str(i)+"image.jpg","wb") as f:
        f.write(re.content)

if __name__ == "__main__":
    for i in range(200):
        get(i)