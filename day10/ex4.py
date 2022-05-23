from pyquery import PyQuery as pq

str = '''
<bookstore>
    <book>
        <title lang="eng">Harry Potter</title>
        <price>29.99</price>
    </book>
    <book>
        <title lang="zh">Learning XML
            <pr2>39.95</pr2>
        </title>
        <price>39.95</price>
      
    </book>
</bookstore>
'''
s = pq(str)  # 初始化
r = s('pr2')  # 选取pr2节点内容
print('1', r)
print(type(r))

r = s('book price')  # CSS选择器
print('2', r)
print(type(r))

print('3', s('book').find('pr2'))  # 在book节点下查找pr2节点
print('4', s('book').children('title'))  # 返回book节点下所有title节点

print('5', s('pr2').parent())  # 父节点
print('6', s('book').parents())  # 祖先节点

aa = s('book > title')
print('7', aa.siblings())  # 定位兄弟节点