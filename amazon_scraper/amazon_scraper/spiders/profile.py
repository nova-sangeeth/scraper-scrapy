import scrapy

from ..items import ProfileItem

class ProfileSpider(scrapy.Spider):
    name = 'profile'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/gp/profile/amzn1.account.AFJGRXKY5QXLUXOS2NHDW3FKNSEA/ref=cm_cr_arp_d_gw_btm?ie=UTF8']
    @staticmethod
    def get_text(selector_list):
        return "".join(selector_list).replace("\n", "").strip()

    def parse(self, response):
        item = ProfileItem()
        for profile in response.css(".desktop padded card dashboard-desktop-card").extract():
            helpful_votes = profile.css(".a-profile-name ::text").extract()
            item["helpful_votes"] = self.get_text(helpful_votes)

            yield item



