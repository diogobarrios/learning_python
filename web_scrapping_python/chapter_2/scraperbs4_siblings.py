from urllib.request import urlopen
from bs4 import BeautifulSoup

# Request the page to crawl
html = urlopen("https://www.pythonscraping.com/pages/page3.html")

# Parsing into BeautifulSoup object
soup = BeautifulSoup(html.read(), 'html.parser')

# Here we get only the rows from the table with id='giftList'
# except the first row
for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)