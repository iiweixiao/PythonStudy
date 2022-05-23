from lxml import etree
import requests

headers = {
    'User-Agent': 'BaiduSpider'
}
index = 1
for page in range(1, 11):
    url = f'https://movie.douban.com/top250?start={(page - 1) * 25}'
    r = requests.get(url, headers=headers)
    # 初始化XPath
    tree = etree.HTML(r.text)
    titles = tree.xpath('//*[@id="content"]/div/div/ol/li/div/div/div/a/span[1]')
    ranks = tree.xpath('//*[@id="content"]/div/div/ol/li/div/div/div/div/span[2]')
    for title, rank in zip(titles, ranks):
        print(index, title.text, rank.text)
        index += 1
