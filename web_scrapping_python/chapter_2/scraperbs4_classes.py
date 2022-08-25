from urllib.request import urlopen
from bs4 import BeautifulSoup

# Open the html page
html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")

# Parser html with BeautifulSoup
bs = BeautifulSoup(html.read(), 'html.parser')

# Getting list of the name, with tagNames and tagAttributes
namelist = bs.findAll('span', {'class': 'green'})

# After getting the list, print the text that has inside of the tag.
for name in namelist:
    print(name.get_text())
