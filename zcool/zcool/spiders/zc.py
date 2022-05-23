import scrapy
from zcool.items import ZcoolItem

count = 1

class ZcSpider(scrapy.Spider):
    name = 'zc'
    allowed_domains = ['zcool.com.cn']
    start_urls = ['https://www.zcool.com.cn/home?p=1#tab_anchor']

    def parse(self, response):
        global count
        count += 1

        divList = response.xpath('//div[@class="sc-hKwDye jgyXZm workList"]/div')
        # print(len(divList))  # 显示40（对应40个封面）就说明上面xpath设置对了
        for div in divList:
            try:
                imgLink = div.xpath('./div[@class="cardImg"]//img/@src').extract_first()
                title = div.xpath('./section/div/span[1]/a/@title').extract_first()
                types = div.xpath('./section/span/@title').extract_first()
                vistor = div.xpath('./section/div[2]/div[1]/@title').extract_first()
                comment = div.xpath('./section/div[2]/div[2]/@title').extract_first()
                likes = div.xpath('./section/div[2]/div[3]/@title').extract_first()

                # [怎么理解下面](https://zhuanlan.zhihu.com/p/351093647#circle=on)
                item = ZcoolItem(imgLink=imgLink, title=title, types=types, vistor=vistor, comment=comment, likes=likes)
                yield item
            except:
                print('e.....')

        next_url = f'https://www.zcool.com.cn/home?p={count}#tab_anchor'
        yield scrapy.Request(next_url)