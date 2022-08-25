from urllib.request import urlopen
from bs4 import BeautifulSoup

# Request the html page to crawl
html = urlopen("https://www.pythonscraping.com/pages/page3.html")

# Parsing into BeautifulSoup object
soup = BeautifulSoup(html.read(), 'html.parser')

# get the price in the first row
# selecting the 'img' -> then parent tag is 'td'
# -> the previous sibling is also a 'td' but the text is the price.
parentSibling = soup.find('img',
                     {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling

# Print the text in the 'td' tag before the 'td' tag
# that contains the image
print(parentSibling.get_text())