from scrapy import Spider, Request
from bestbuy.items import BestbuyItem
import re

class PowellSpider(Spider):
    name = 'powell_spider'
    allowed_domains = ['www.powells.com']
    start_urls = ['https://www.powells.com/used']

    def parse(self, response):
        # Find the total number of pages in the result so that we can decide how many urls to scrape next
        text = response.xpath('//div[@class="left-side"]/span/text()').extract_first()
        _, per_page, total = map(lambda x: int(x), re.findall('\d+', text))
        number_pages = total // per_page

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
