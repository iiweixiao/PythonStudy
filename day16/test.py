from lxml import etree
text = '''
<bookstore>
    <book>
      <title lang="eng">Harry Potter</title>
      <price>29.99</price>
    </book>
    <book>
      <title lang="zh">Learning XML</title>
      <price>39.95</price>
    </book>
</bookstore>
'''

html = etree.HTML(text)

res = etree.tostring(html)

# print(res.decode('utf-8'))

res = html.xpath('//*')
print(res)

# # 初始化xpath
# html = etree.HTML(response.text)
# # xpath()进行节点定位
# result = html.xpath('//*')
# # xpath()进行节点定位
# result1 = html.xpath('//li')[0]
# # 选取所有的子节点 / 获取子节点 // 获取所有的子孙节点
# result2 = html.xpath("//li/a")
# # .. 寻找父节点
# result3 =html.xpath('//a[@href="/sites/the-shift-1"]/../@class')
# # @过滤属性
# result4 = html.xpath('//li[@class="col-3"]')
# # text() 获取文本信息
# result5 = html.xpath('//div[@class="row"]/h3/a/text()')[1]
# # text() 获取属性
# result6 = html.xpath('//li//a/@href') # [@href="awwwards/collections/free-fonts/"]
# # 多值匹配
# result7 = html.xpath('//div[contains(@class, "row")]/div/text()')
# # 多属性匹配
# result8 = html.xpath('//div[contains(@class, "item") and @data-username="Archrival"]/a/@href')
# # 按序匹配 取第一个li节点
# result9 = html.xpath('//li[1]/div/a/@href')
# # 最后一个li节点
# result10 = html.xpath("//li[last()]/a/text()")
# # 位置小于3的li节点
# result11 = html.xpath("//li[position()<3]/a/text()")
# # 倒数第三个li节点
# result12 = html.xpath('//li[last()-2]/a/text()')
# # 节点轴
# result13 = html.xpath("//li[1]/ancestor::*") # 获取所有祖先节点
# result14 = html.xpath("//li[1]/ancestor::div")  # 获取div祖先节点
# result15 =html.xpath("//li[1]/attribute::*") # 获取所有属性值
# result16 = html.xpath("//li[1]/child::*") # 获取所有直接子节点
# result17 = html.xpath("//li[1]/descendant::a") # 获取所有子孙节点的a节点
# result18 = html.xpath("//li[1]/following::*") # 获取当前子节点之后的所有节点