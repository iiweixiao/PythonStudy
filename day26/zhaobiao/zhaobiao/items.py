# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaobiaoItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    place = scrapy.Field()
    industry = scrapy.Field()
