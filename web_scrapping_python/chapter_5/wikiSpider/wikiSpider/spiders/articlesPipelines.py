from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article

class ArticleSpider(CrawlSpider):
    """Rules of the game"""
    name = 'articlesPipelines'
    allowed_domains = ['wikipedia.org']  # Which domain to fix
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']  # Where to start crawling
    rules = [
        Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'), callback='parse_items', follow=True),
        ] 


    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.xpath('//h1/span/text()').get()
        article['text'] = response.xpath('//div[@class="mw-parser-output"]//text()').get()
        lastUpdated = response.css('li#footer-info-lastmod::text').get()
        return article

