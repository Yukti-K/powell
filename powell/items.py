# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PowellItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()
    quantity = scrapy.Field()
    stores = scrapy.Field()
    pub_date = scrapy.Field()
    pub = scrapy.Field()
    rating = scrapy.Field()
    comment = scrapy.Field()

    yield item