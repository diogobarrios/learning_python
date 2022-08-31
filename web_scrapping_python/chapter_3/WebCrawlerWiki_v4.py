from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# Random-number generator seed with the current sys time.
# Ensures a new and interesting random path through Wikipedia articles
# every time the program is run
random.seed(datetime.datetime.now())

# Function that gets the links from the loop that initializes with
# /wiki/kevin_Bacon
def getLinks(articleUrl):
    # Request the page 
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    # Parsing to BeautifulSoup object
    soup = BeautifulSoup(html.read(), 'html.parser')
    # find all 'a' tags with attr 'href'
    return soup.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

# Start with this link
links = getLinks('/wiki/Kevin_Bacon')

# Then loop through the links extract in 'links'
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)