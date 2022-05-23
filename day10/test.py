from bs4 import BeautifulSoup  # pip install bs4
import requests
from lxml import etree

"""  
解析器               使用方法  
python标准库           BeautifulSoup(markup, "html.parser")lxml HTML 解析器       BeautifulSoup(markup, "lxml")lxml XML 解析器       BeautifulSoup(markup, "XML")html5lib            BeautifulSoup(markup, "html5lib")  

"""
url = "https://cs.58.com/"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

h1 = requests.get(url, headers=headers)



# print(html)
# res = html.xpath('//*')
# print(res)




# print(type(html))
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p)  # <p class="micoNewTxt">新版</p>
# print(soup.p.string)  # 新版
# print('-' * 30)