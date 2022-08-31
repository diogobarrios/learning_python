from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Request the page 
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")

# Parsing to BeautifulSoup object
soup = BeautifulSoup(html.read(), 'html.parser')

# find all 'a' tags with attr 'href'
for link in soup.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])