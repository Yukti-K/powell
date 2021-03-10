# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PowellItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titles = scrapy.Field()
    reg_prices = scrapy.Field()
    disc_prices = scrapy.Field()
    categories = scrapy.Field()
    authors = scrapy.Field()