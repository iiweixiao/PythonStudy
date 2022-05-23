from scrapy.selector import Selector

doc = ''
with open('./test.html', 'r') as f:
    doc = f.read()

sel = Selector(text=doc)
print(sel)

# res = sel.xpath('//div[@class="cdiv"]//li').get()
# print(res)
#
# # res = sel.re(r'class="item (.*?)">')
# res = sel.re(r'cli-\d">')
# print(res)

res = sel.xpath('//li[3]')
print(res)
