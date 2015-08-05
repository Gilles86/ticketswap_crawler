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

        # Discard the last 5 ones ('verkocht')
        for sel in response.xpath('//section[@class = "ad-list"]/article[@itemprop="tickets"]')[:-5]:
            item = items.TicketswapCrawlerItem()
            print sel
            item['id'] = sel.xpath('a[@itemprop = "offerurl"]/@href').re(r'/tickets/([0-9]+)/.*')[0]
            #item['description'] = sel.xpath('div/span/a[@itemprop = "offerurl"]/text()').extract()[0]
            item['quantity'] = sel.xpath('.//meta[@itemprop="quantity"]/@content').extract()[0]
            item['price'] = sel.xpath('.//meta[@itemprop = "price"]/@content').extract()[0]
            item['user'] = sel.xpath('.//div[@class = "ad-list-user"]/div[@class = "name"]/text()').extract()[0]
            item['time'] = str(datetime.datetime.now())
            yield item

