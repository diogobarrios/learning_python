from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


pages = set()
def getLinks(pageUrl):
    global pages
    # Request the page 
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    # Parsing to BeautifulSoup object
    soup = BeautifulSoup(html, 'html.parser')
    # Loop for finding links which starts with '/wiki/'
    for link in soup.find_all('a', href=re.compile('^/wiki/')):
        # if link has 'href' attr
        if 'href' in link.attrs:
            # and is not in pages set
            if link.attrs['href'] not in pages:
                # We have encountered a new page
                # Create a 'newPage'
                newPage = link.attrs['href']
                print(newPage)
                # And add to the set
                pages.add(newPage)
                # search links with this new one
                getLinks(newPage)

getLinks('')