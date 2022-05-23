from lxml import etree

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

h = etree.HTML(str)
r = h.xpath('//*')
print('1', r)
print(type(r))
r = h.xpath('//book/pr2')
print('2', r)
print(type(r))
r = h.xpath('//pr2/..')
print('3', r)
print(type(r))
r = h.xpath('//title[@lang="zh"]')
print('4', r)
print(type(r))
r = h.xpath('//book/title/text()')[1]
print('5', r)
print(type(r))
r = h.xpath('//bookstore//title/@lang')
print('6', r)
print(type(r))
