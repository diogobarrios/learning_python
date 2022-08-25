from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Reques the html page
html = urlopen(" http://www.pythonscraping.com/pages/page3.html")

# Parsing it to BeautifulSoup object
soup = BeautifulSoup(html.read(), 'html.parser')

# Find all the url's from the images within the table of products
images = soup.find_all('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})

# Display the list of the url's crawled
for image in images:
    print(image['src'])