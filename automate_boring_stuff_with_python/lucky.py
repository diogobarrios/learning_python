#! python3
# lucky.py - Opens several Google search results

import requests
import sys
import webbrowser
import bs4

print('Googling...')  # Display text while downloading the Google page

# specify browser user-agent, Google will treat it as a "user"
# if not specify google will catch the python bot.
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
           }
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]),
                   headers=headers)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')


# Step 1: Get the links #href from search:
list_href = []
# How many tags 'a' has on the first page of google?
for link in range(len(soup.select('a'))):
    # In that 'a' tags if it has 'h3' tags...
    if (soup.select('a')[link]).find('h3') != None:
        # get 'href' tag from each 'a' tag that has 'h3' tags
        list_href.append(soup.select('a')[link].get('href'))
    else:
        # Only to know...
        print('Not this ' + str(link))

# Step 2: Open Web Browser for Each Result

num_open = min(4, len(list_href))
for i in range(num_open):
    webbrowser.open(list_href[i])
