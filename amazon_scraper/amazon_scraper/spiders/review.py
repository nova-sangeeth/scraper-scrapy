import scrapy
from ..items import AmazonScraperItem
from scrapy.http import Request
import logging


class ReviewSpider(scrapy.Spider):
    name = "review"
    allowed_domains = ["amazon.com"]
    start_urls = [
        'https://www.amazon.com/Portable-Charger-Anker-PowerCore-20100mAh/product-reviews/B00X5RV14Y/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    ]

    @staticmethod
    def get_text(selector_list):
        return "".join(selector_list).replace("\n", "").strip()
    # working on the empty data and depth of the scraping that happens during a session
    def parse(self, response):
        item = AmazonScraperItem()
        for review in response.css(".review"):
            redirect_urls = response.request.meta.get('redirect_urls')
            author = review.css(".a-profile-name ::text").extract()
            item["author"] = self.get_text(author)

            author_profile_url = review.css(" a.a-profile ::attr(href)").extract()
            item["author_profile_url"] = self.get_text(author_profile_url)

            title = review.css(".review-title-content span ::text").extract()
            item["title"] = self.get_text(title)

            review_content = review.css(".review-text-content ::text").extract()
            item["review_content"] = self.get_text(review_content)

            verified = review.css(".review-format-strip ::text").extract()
            item["verified"] = self.get_text(verified)

            rating = review.css(".review-rating span ::text").extract()
            item["rating"] = self.get_text(rating)

            date_of_review = review.css(".review-date ::text").extract()
            item["date_of_review"] = self.get_text(date_of_review)

            votes_helpful = review.css(".cr-vote-text ::text").extract()
            item["votes_helpful"] = self.get_text(votes_helpful)

            image_num = review.css(".review-image-tile-section ::attr(src)").extract()
            item["image_num"] = len(image_num)

            num_of_comments = review.css(".review-comment-total ::text").extract()
            item["num_of_comments"] = self.get_text(num_of_comments)

            item['pageURL'] = redirect_urls[0] if redirect_urls else response.request.url

            yield item

        next_page = response.css(
            "#cm_cr-pagination_bar > ul > li.a-last > a ::attr(href)"
        ).get()
        if next_page:
            abs_url = f"https://www.amazon.com{next_page}"
            yield scrapy.Request(url=abs_url, callback=self.parse)
        else:
            logging.warning("Watch out! No pages left.")
