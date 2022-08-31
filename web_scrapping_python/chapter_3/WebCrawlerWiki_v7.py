from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

from WebCrawlerWiki_v6 import getExternalLinks, getInternalLinks


random.seed(datetime.datetime.now())

allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)


allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')