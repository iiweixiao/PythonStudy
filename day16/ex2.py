import requests
from lxml import etree
from urllib import request
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.huya.com/g/1663'

html = requests.get(url)
data = etree.HTML(html.text)
res = data.xpath('//li[@class="game-live-item"]')

if not os.path.exists('image/'):
    os.mkdir('image/')

for i in res:
    d = i.xpath('./a[1]/img[@class="pic"]/@data-original')[0]
    t = i.xpath('./a[2]/text()')[0]
    try:
        request.urlretrieve(d, 'image/' + t + '.jpg')
    except:
        print('e...')
