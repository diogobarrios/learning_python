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
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:],
                                                                 headers=headers))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
# <h3 class="LC20lb MBeuO DKV0Md">...</h3>
link_elems = soup.select('a href')
