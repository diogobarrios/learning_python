from urllib.request import urlopen
from bs4 import BeautifulSoup

# request html page
html = urlopen(" http://www.pythonscraping.com/pages/page3.html")

# Parser with bs object
bs = BeautifulSoup(html.read(), 'html.parser')

# get all children that in the table with id='giftList'
# and not descendants, that would retrieve it more
for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)