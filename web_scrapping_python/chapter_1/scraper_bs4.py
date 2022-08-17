from urllib.request import urlopen
from bs4 import BeautifulSoup

# Open the html page and save into a variable
html = urlopen("http://pythonscraping.com/pages/page1.html")

# Call html.read() to get the content of the page.
# BeautifulSoup transform into bs object with a more pleasant structure.
bs = BeautifulSoup(html.read(), 'html.parser')
# Could be with a variant a powerful than html.parser for 'messy' html code.
# bs = BeautifulSoup(html.read(), 'lxml') 
# But it needs to be installed, like, pip3 install lxml

# Print the h1 tag
print(bs.h1)
# These variants will produce the same output too
print(bs.html.body.h1)
print(bs.html.h1)
print(bs.body.h1)