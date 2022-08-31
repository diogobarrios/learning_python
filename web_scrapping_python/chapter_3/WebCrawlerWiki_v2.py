from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Request the page 
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")

# Parsing to BeautifulSoup object
soup = BeautifulSoup(html.read(), 'html.parser')

# find the parent 'div' tag with 'id'='bodyContent
# then within find_all 'a' tags with attr href that starts with /wiki/, doesn't have ':'
# and then if this attr is in the link, print them. 
for link in soup.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])