
import requests
from bs4 import BeautifulSoup


class Content:
    """
    Common base class for all articles/pages
    """
   
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
    

    def print(self):
        """
        Flexible printing function controls output
        """
        print("URL: {}".format(self.url))
        print("Title: {}".format(self.title))
        print("Body {}".format(self.body))


class Website:
    """
    Contains information about website structure
    """

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:
    """
    Parsing the url and get desire information
    """
    
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
    

    def SafeGet(self, pageObj, selector):
        """
        Utility function to get a content string from a 
        Beautiful Soup object and a selector. Returns an 
        empty string if no object is found for the given selector
        """
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    
    def parse(self, url, site):
        """
        Extract content from a given page URL
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.SafeGet(bs, site.titleTag)
            body = self.SafeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()


crawler = Crawler()


siteData = [
        ["O'Reilly Media", 'http://oreilly.com','h1', 'section#product-description'],
        ['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body_1gnLA'],
        ['Brookings', 'http://www.brookings.edu', 'h1', 'div.post-body'],
        ['New York Times', 'http://nytimes.com', 'h1', 'p.story-content']
]


websites = []
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')
crawler.parse(websites[1], 'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(websites[2], 'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(websites[3], 'https://www.nytimes.com/2018/0128/business/energy-environment/oil-boom.html')
