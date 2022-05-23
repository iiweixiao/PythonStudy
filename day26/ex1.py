import os.path
import openpyxl
import requests
from lxml import etree


url = 'https://www.chinabidding.cn/search/searchgj/zbcg?keywords=%E8%AF%95%E9%AA%8C%E6%9C%BA'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
}

html = requests.get(url, headers=headers)
# print(html)
data = etree.HTML(html.text)
res = data.xpath('//div[@class="lieb"]/table/tbody/tr/td/table/tbody')
if not os.path.exists('data/'):
    os.mkdir('data/')
for i in res:
    titles = i.xpath('//tr//a/@title')
    places = i.xpath('//tr/td[5]/text()')
    industries = i.xpath('//tr/td[6]/text()')

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'zhaobiao'
sheet.append(('标题', '地点', '行业'))
zi = zip(titles, places, industries)
for title, place, industry in zi:
    sheet.append((title, place, industry))
wb.save('招标.xlsx')