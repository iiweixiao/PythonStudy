import urllib.request

# 请求的url
url = 'https://movie.douban.com/'


# 自定义请求头信息
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/94.0.4606.81 Safari/537.36',
    'Referer': 'https://www.baidu.com/link?url=I2OFtFqDOzZvlDKHhQgcnbKbADSXtLh-oZJAQiBNGrgPSl-16z_HD1cxg8cX-VvG&wd=&eqid=b37cb5fd00012fa5000000066166d9be',
    'Connection': 'keep-alive'
}

# 设置 Request 的请求头
req = urllib.request.Request(url,headers=headers)

# 使用urlopen 打开 req
html = urllib.request.urlopen(req).read().decode('utf-8')

# 写入文件
f = open("html.txt",'w',encoding="utf-8")
f.write(html)
f.close()