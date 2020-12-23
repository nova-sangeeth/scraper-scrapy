# <Down>Define here the models for your scraped items

# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScraperItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    author_profile_url = scrapy.Field()
    title = scrapy.Field()
    review_content = scrapy.Field()
    verified = scrapy.Field()
    rating = scrapy.Field()
    date_of_review = scrapy.Field()
    votes_helpful = scrapy.Field()
    image_num = scrapy.Field()
    num_of_comments = scrapy.Field()
    pageURL = scrapy.Field()


class ProfileItem(scrapy.Item):
    helpful_votes = scrapy.Field()
    total_review = scrapy.Field()
    page_url = scrapy.Field()

class rankingItem(scrapy.Item):
    ranking = scrapy.Field()
    page_url = scrapy.Field()