from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    """Rules of the game"""
    name = 'articlesMoreRules'
    allowed_domains = ['wikipedia.org']  # Which domain to fix
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']  # Where to start crawling
    rules = [
        Rule(LinkExtractor(allow='^(/wiki/)((?!:).)*$'), callback='parse_items', follow=True, cb_kwargs={'is_article': True}),
        Rule(LinkExtractor(allow='.*'), callback='parse_items', follow=True, cb_kwargs={'is_article': False})
        ] 


    def parse_items(self, response, is_article):
        print(response.url)
        title = response.xpath('//h1/span/text()').get()
        if is_article:
            url = response.url
            text = response.xpath('//div[@class="mw-parser-output"]//text()').get()
            lastUpdated = response.css('li#footer-info-lastmod::text').get()
            lastUpdated = lastUpdated.replace('This page was last edited on', '')
            print('URL is: {}'.format(url))
            print('title is: {}'.format(title))
            print('text is: {}'.format(text))
            print('Last updated: {}'.format(lastUpdated))
        else:
            print('This is not an article: {}'.format(title))

