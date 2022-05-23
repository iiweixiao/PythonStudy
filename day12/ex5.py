# 复习xpath
# 虎牙图片
import requests
from lxml import etree
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.huya.com/g/4079'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}

html = requests.get(url, headers=headers).text

data = etree.HTML(html)

urls = data.xpath('//*[@id="js-live-list"]/li/a[1]/img/@data-original')
name = data.xpath('//*[@id="js-live-list"]/li/a[1]/img/@alt')
title = data.xpath('//*[@id="js-live-list"]/li/a[2]/@title')
n = len(urls)
for i in range(n):
    # print(name[i], "\t", title[i], urls[i])
    request.urlretrieve(urls[i], '/Users/abc/Desktop/test/' + name[i] + '.jpg')
