from bs4 import BeautifulSoup

str = '''
<bookstore>
    <book>
      <title lang="eng">Harry Potter</title>
      <price>29.99</price>
    </book>
    <book>
      <title lang="zh">Learning XML</title>
        <pr2>39.95</pr2>
      <price>39.95</price>
      
    </book>
</bookstore>
'''
s = BeautifulSoup(str, 'lxml')  # lxml HTML解析器固定格式

r = s.select('book')
print('1', r)
print(type(r))
r = s.select('book > title')
print('2', r)
print(type(r))
r = s.select('bookstore title')
print('3', r)
print(type(r))
