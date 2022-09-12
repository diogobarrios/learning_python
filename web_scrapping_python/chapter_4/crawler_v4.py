
from urllib.parse import non_hierarchical
import requests
from bs4 import BeautifulSoup
import re

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

    def __init__(self, name, url, targetPattern, absoluteUrl ,titleTag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern      
        self.absoluteUrl = absoluteUrl       # is a boolean that tells whether these search results are abs ou rel URLs
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:
    """
    Parsing the url and get desire information
    """
    def __init__(self, site):
        self.site = site
        self.visited = []


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

    def parser(self, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
    
    def crawl(self):
        """
        get pages from website home page
        """
        bs = self.getPage(self.site.url)
        targetPages = bs.find_all('a', href=re.compile(self.site.targetPattern))
        for targetPage in targetPages:
            targetPage = targetPage.attrs['href']
            if targetPage not in self.visited:
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = '{}{}'.format(self.site.url, targetPage)
                self.parse(targetPage)



reuters = Website('Reuters', 'https://www.reuters.com', '^(/article/)', False, 'h1', 'div.StandardArticleBody_body_1gnLA')

crawler = Crawler(reuters)
crawler.crawl()