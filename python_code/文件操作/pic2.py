import requests
import json
import urllib

def getSogouImag(category,length,path):
    n = length
    cate = category
    imgs = requests.get('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['bthumbUrl'])
    count = 0
    for img_url in imgs_url:
            print('***** '+str(count)+'.jpg *****'+'   Downloading...')
            urllib.request.urlretrieve(img_url,path+str(count)+'.jpg')
            count = count + 1
    print('Download complete!')

getSogouImag('壁纸',20,'C:/Users/hp/Desktop/picture/')