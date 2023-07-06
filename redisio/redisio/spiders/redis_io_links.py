from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RedisIoLinkSpider(CrawlSpider):
    name = "redis_io_links"
    allowed_domains = ["redis.io"]
    start_urls = ["https://redis.io"]
    handle_httpstatus_list = [404]

    rules = (
        Rule(LinkExtractor(allow="/docs"), callback="parse_items", follow=True),
        Rule(LinkExtractor(allow="/commands"), callback="parse_items", follow=True),
        Rule(LinkExtractor(allow="/resources"), callback="parse_items", follow=True),
        Rule(LinkExtractor(allow="/community"), callback="parse_items", follow=True),
        Rule(LinkExtractor(allow="/support"), callback="parse_items", follow=True),
    )


    def parse_items(self, response):
        
        url = str(response.url)
        status = int(response.status)

        yield {
           "status": status,
           "url": url
        }



