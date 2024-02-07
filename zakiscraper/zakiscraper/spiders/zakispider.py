import scrapy


class ZakispiderSpider(scrapy.Spider):
    name = "zakispider"
    # should be a list of allowed domains
    allowed_domains = ["https://parts.expert/en"]
    start_urls = ["https://parts.expert/en"]  # should be a list of start_urls

    # go through each loop
    # get item name and price
    # store
    # draft in a graph

    def parse(self, response):
        nav_static = response.css('a.nav-static')
        for menu in nav_static:
            item = menu.css(
                'article.Product-wrapper js-block-product-card Product-wrapper--pdt')
