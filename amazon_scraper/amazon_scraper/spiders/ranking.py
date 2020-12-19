import scrapy


class RankingSpider(scrapy.Spider):
    name = 'ranking'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
