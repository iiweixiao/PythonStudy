import requests
import json
from urllib import request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56'
}

if not os.path.exists('image/'):
    os.mkdir('image/')
n = 0
while n < 5:

    url = f'https://image.so.com/zjl?sn={n*30}&ch=car'
    html = requests.get(url).text
    data = json.loads(html)
    lst = data['list']
    for i in lst:
        title = i['pic_desc']
        pic_url = i['qhimg_downurl']
        # print(pic_url)
        try:
            request.urlretrieve(pic_url, 'image/' + title + '.jpg')
        except:
            print('e......')
    n += 1