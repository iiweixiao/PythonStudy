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
r = s('book')  # 单个book节点
l = s('title').items()  # 将所有title节点保存到PyQuery.items
print('1', l)
for i in l:  # 遍历title节点
    print(i)
print('2', end=' ')

# print(i for i in s('bookstore > book > title').items())  # 表达式有误，输出不了
l = s('bookstore > book > title').items()
print(l)
for i in l:
    print(i)

print([i for i in range(10)])  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
aa = (i for i in range(10))  # 将不再生成列表，而是一个生成器
for a in aa:
    print(a, end=' ')
