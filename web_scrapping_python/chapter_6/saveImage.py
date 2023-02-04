from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')

# Because the name of the class is to big
class_tag_a = 'pagelayer-wp-title-link pagelayer-ele-link pagelayer-wp-title-align-left pagelayer-wp-title-vertical-middle'

imageLocation = bs.find('a', {'class': class_tag_a}).find('img')['src']
urlretrieve(imageLocation, 'logo.jpg')