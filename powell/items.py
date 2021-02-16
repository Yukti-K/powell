# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PowellItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item = PowellItem()
    item['title'] = title
    item['price'] = price
    item['author'] = author
    item['category'] = category
    item['quantity'] = quantity
    item['stores'] = stores
    item['pub_date'] = pub_date
    item['pub'] = pub
    item['rating'] = rating
    item['comment'] - comment

    yield item