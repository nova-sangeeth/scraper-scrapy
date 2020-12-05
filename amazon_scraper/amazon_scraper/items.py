# <Down>Define here the models for your scraped items

# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScraperItem(scrapy.Item):
    # define the fields for your item here like:
    reviewer = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    date_of_review = scrapy.Field()
    verified_review = scrapy.Field()
    review = scrapy.Field()
    votes = scrapy.Field()
    comments = scrapy.Field()


class AmazonProfileItem(scrapy.Item):
    review_ranking = scrapy.Field()
    number_of_votes = scrapy.Field() 
    ranking = scrapy.Field()
