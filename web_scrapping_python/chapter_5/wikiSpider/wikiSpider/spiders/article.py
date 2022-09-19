"""Example of a limited spyder to look for article"""

import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Python_(programming_language)',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python'
        ]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls] # List comprehension
    

    def parse(self, response):
        url = response.url
        title = response.xpath('//h1/span/text()').get() #extract_first() was changed to .get() method for readibility
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))