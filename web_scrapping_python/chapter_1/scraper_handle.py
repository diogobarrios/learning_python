from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    # if I receive an HTTP error I will handle wih HTTPError
    except HTTPError as e:
        print("HTTP not found")
        
    # if the url isn't working, mistyped I will handle with URLError
    except URLError as e:
        print("The server could not be found!")

    # but could work too
    else:
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')
            title = bs.body.h1
        except AttributeError as e:
            return None
        return title


# HTTPError example
# title = getTitle("http://pythonscraping.com/pages/donotexist/page1.html")

# URLError example
# title = getTitle('https://pythonscrapingthisurldoesnotexist.com')

# working example
title = getTitle("http://pythonscraping.com/pages/page1.html")

if title == None:
    print('Title could not be found')
else:
    print(title)