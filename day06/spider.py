import requests  # 发送请求
from lxml import etree  # 数据筛选模块
from urllib import request  # 下载模块

# 1. 确定网址
url = 'https://www.huya.com/g/4079'

# 2. 发送请求 - 接受响应
result = requests.get(url)
# print(result)
# print(result.text)

# 3. 筛选数据
# xpath json re pyquery bs4
data = etree.HTML(result.text)
# print(data)

res = data.xpath("//img[@class='pic']")
# print(res\)

# 4. 保存数据
for i in res:
    newUrl = i.xpath('./@data-original')