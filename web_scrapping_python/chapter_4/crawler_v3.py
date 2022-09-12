
import requests
from bs4 import BeautifulSoup


class Content:
    """
    Common base class for all articles/pages
    """
   
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body
    

    def print(self):
        """
        Flexible printing function controls output
        """
        print("New article found for topic: {}".format(self.topic))
        print("URL: {}".format(self.url))
        print("Title: {}".format(self.title))
        print("Body {}".format(self.body))


class Website:
    """
    Contains information about website structure
    """

    def __init__(self, name, url, searchUrl, resultListing, 
    resultUrl, absoluteUrl ,titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl           # defines where go search results appending the topic
        self.resultListing = resultListing   # defines the 'box' that holds the information about each result
        self.resultUrl = resultUrl           # defines the tag inside the 'box' that will give the exact URL
        self.absoluteUrl = absoluteUrl       # is a boolean that tells whether these search results are abs ou rel URLs
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
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''

    
    def search(self, topic, site):
        """
        Searches a given website for a given topic and records all pages found
        """
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs['href']
            # check to see whether it's a relative or an absolute URL
            if(site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print("Something was wrong with that page or URL. Skipping!")
                return
            title = self.SafeGet(bs, site.titleTag)
            body = self.SafeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, title, body, url)
                content.print()


crawler = Crawler()


siteData = [
['O\'Reilly Media', 'http://oreilly.com', 'https://ssearch.oreilly.com/?q=','article.product-result',
    'p.title a', True, 'h1', 'section#product-description'],
['Reuters', 'http://reuters.com', 'http://www.reuters.com/search/news?blob=', 'div.search-result-content',
    'h3.search-result-title a', False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
['Brookings', 'http://www.brookings.edu', 'https://www.brookings.edu/search/?s=', 'div.list-content article',
    'h4.title a', True, 'h1', 'div.post-body']
]

sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']
for topic in topics:
    print("Getting info about: " + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)
