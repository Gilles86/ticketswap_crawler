# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from ticketswap_crawler import items
import datetime

class TicketSwapSpider(scrapy.Spider):
    name = "ticketswap"
    allowed_domains = ["ticketswap.nl"]
    start_urls = [
        "https://www.ticketswap.nl/lowlands/festival"
    ]

    def parse(self, response):
        
        print 'yoyoyoy'

        for sel in response.xpath('//section[@class = "ad-list"]'):
            item = items.TicketswapCrawlerItem()
            item['id'] = sel.xpath('div/span/a[@itemprop = "offerurl"]/@href').re(r'/tickets/([0-9]+)/.*')[0]
            #item['description'] = sel.xpath('div/span/a[@itemprop = "offerurl"]/text()').extract()[0]
            item['quantity'] = sel.xpath('div/span[@itemprop = "quantity"]/text()').re('.*([0-9]+).*')[0]
            item['price'] = sel.xpath('div/meta[@itemprop = "price"]/@content').extract()[0]
            item['user'] = sel.xpath('div[@class = "user"]/span[@class = "value"]/text()').extract()[0]
            item['time'] = str(datetime.datetime.now())
            yield item

