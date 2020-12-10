import scrapy
import json
from ..items import ProfileItem
filename = '/home/nova/webdev-lessons/web_scraper/amazon_scraper/amazon-profile-url.txt'
class ProfileSpider(scrapy.Spider):
    name = 'profile'
    allowed_domains = ['amazon.in']
    # start_urls = [
    #     'https://www.amazon.in/hz/gamification/api/contributor/dashboard/amzn1.account.AGHOJQ4IOQAGANGL6RYNRO7SYADA',
    #     'https://www.amazon.in/hz/gamification/api/contributor/dashboard/amzn1.account.AEJH7F5LBTU6KDEECRJUZIVSZINA',
    #     'https://www.amazon.in/hz/gamification/api/contributor/dashboard/amzn1.account.AEWUQHUYUCFGCMUBAGGKWUY27TKA',
    #     'https://www.amazon.in/hz/gamification/api/contributor/dashboard/amzn1.account.AEWUQHUYUCFGCMUBAGGKWUY27TKA',
    #     'https://www.amazon.in/hz/gamification/api/contributor/dashboard/amzn1.account.AH6LMXTC7N4EZNCFG2SEBOWTJFUQ',
    #     ]
    def __init__(self, filename=filename):
        if filename:
                with open(filename, 'r') as r:
                    self.start_urls = r.readlines()

    def parse (self, response):
        item = ProfileItem()
        resp = json.loads(response.body)
        helpful = resp.get('helpfulVotes').get('helpfulVotesData').get('count')
        item['helpful_votes'] = helpful
        helpful = resp.get('reviews').get('reviewsCountData').get('count')
        item['total_review'] = helpful
        yield item
            