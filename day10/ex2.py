import re

from bs4 import BeautifulSoup

str = '''
<bookstore>
    <book>
      <title lang="eng">Harry Potter</title>
      <price>29.99</price>
    </book>
    <book>
      <title lang="zh">Learning XML</title>
        <pr2 href='http://www.baidu.com'>39.95</pr2>
      <price>39.95</price>
      
    </book>
</bookstore>
'''
s = BeautifulSoup(str, 'lxml')  # lxml HTML解析器固定格式

print('1', s.title)
print(type(s.title))

print('2', s.text.strip())
print(type(s.text))
# prettify() 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行
# BeautifulSoup 对象和它的tag节点都可以调用 prettify() 方法
print('3', s.price.prettify())
print('4', s.prettify())
# 节点选择器
print('5', s.title.string)
print('6', s.title['lang'])  # 只取第一个'eng'，取不到'zh'

print('7', s.book.contents)  # book节点下的内容
print('8', s.book.children)  # 子节点
for i, child in enumerate(s.book.children):
    print('\t', i, child)

print('9', s.book.descendants)  # 得到所有的子孙节点
for i, child in enumerate(s.book.descendants):
    print('\t', i, child)
print('10', s.book.parents)
# find_all方法
print('11', s.find_all(name='title'))  # 返回列表
print('12', s.find_all(attrs={'lang': 'zh'}))
# find方法
print('13', s.find('pr2'))
print('14', s.find(name='title'))
