import scrapy
from .. items import AmazonProfileItem

class ProfileSpider(scrapy.Spider):
    name = 'profile'
    # allowed_domains = ['example.com']
    start_urls = ['https://www.amazon.in/gp/profile/amzn1.account.AEQWFRM5IA7FG7DCJTEWAPYUOSAQ/ref=cm_cr_arp_d_gw_btm?ie=UTF8']

    def parse(self, response):
        profile = AmazonProfileItem()

        review_ranking = response.css('.a-size-base').css('::text').extract()
        num_of_reviews = response.css('.large-margin-right:nth-child(1) .a-size-large').css('::text').extract()
        reviewer_ranking = response.css('.a-span12 .a-size-base::text').extract()

        profile['review_ranking'] = review_ranking
        profile['num_of_reviews'] = num_of_reviews
        profile['reviewer_ranking'] = reviewer_ranking
        yield profile
