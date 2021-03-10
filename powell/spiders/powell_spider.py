from scrapy import Spider, Request
from powell.items import PowellItem
import re

class PowellSpider(Spider):
    name = 'powell_spider'
    allowed_domains = ['www.powells.com']
    start_urls = ['https://www.powells.com/used']

    def parse(self, response):
        # Find the total number of pages in the result so that we can decide how many urls to scrape next
        page1 = 'https://www.powells.com/used'
        page_parts = ['','?mpp=50&pg=2','?mpp=50&pg=3','?mpp=50&pg=4','?mpp=50&pg=5','?mpp=50&pg=6','?mpp=50&pg=7','?mpp=50&pg=8','?mpp=50&pg=9','?mpp=50&pg=10','?mpp=50&pg=11','?mpp=50&pg=12','?mpp=50&pg=13','?mpp=50&pg=14','?mpp=50&pg=15','?mpp=50&pg=16','?mpp=50&pg=17','?mpp=50&pg=18','?mpp=50&pg=19','?mpp=50&pg=20']
        url_list = [str(page1 + page) for page in page_parts]

        for url in url_list:
            yield Request(url=url,callback=self.parse_result_page)

    def parse_result_page(self,response):
        rows = response.xpath('//div[@class="book-details"]')
        for row in rows:

            try:
                titles = row.xpath('./div[@class="book-title-wrapper"]//a/text()').extract()[0]
                authors =   row.xpath('./div[@class="book-author"]/text()').extract_first()
                categories = row.xpath('./div[@class="book-type"]/text()').extract_first()
                reg_prices = row.xpath('.//span[@class="strikethrough"]/text()').extract_first()
                disc_prices = row.xpath('//div[@class="disc-price"]/text()').extract_first().strip()

            except Exception as e:
                print(e)

            item = PowellItem()
            item['titles'] = titles
            item['reg_prices'] = reg_prices
            item['disc_prices'] = disc_prices
            item['authors'] = authors
            item['categories'] = categories
     
            yield item
