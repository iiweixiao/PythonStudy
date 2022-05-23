import requests  # 发送请求
from lxml import etree  # 数据筛选模块
from urllib import request  # 下载模块
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 1. 确定网址
url = 'https://www.huya.com/g/4079'

# 2. 发送请求 - 接受响应
result = requests.get(url, verify=False)
# print(result)
# print(result.text)

# 3. 筛选数据
# xpath json re pyquery bs4
data = etree.HTML(result.text)  # 使用lxml中的etree模块可以对HTML中的节点进行补全
print(data)
print(type(data))
res = data.xpath("//img[@class='pic']")
print(res)

# # 4. 保存数据
for i in res:
    newUrl = i.xpath('./@data-original')[0]
#     newName = i.xpath('./@alt')[0]
    print(newUrl)
#     request.urlretrieve(newUrl, '/Users/brucewei/Desktop/test/' + newName + '.jpg')
#     # Windows下，目录格式用了反斜杠，连接必须要用'\\'。
#     # request.urlretrieve(newUrl, r'\Users\brucewei\Desktop\test\\' + newName + '.jpg')