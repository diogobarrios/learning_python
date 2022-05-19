#! Python3

# xkcd.py - Download webcomcis from https://xkcd.com/

import bs4
import requests
import os

# re.compile(r'[^//imgs.xkcd.com/comics/]([A-Za-z0-9].+.png)')

# soup.find_all('img')[2].get('src')

url = 'http://xkcd.com'  # starting url
os.makedirs('xkcd, exist_ok=True')  # store conics in ./xkcd

while not url.endswith('#'):
    #  Download the page.
    print('Dowloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image.
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image')
    else:
        comic_url = comic_elem[0].get('src')
        # Download the image.
        print('Dowloading image %s...' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()
        # Save the image to ./xkcd.
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)),
                          'wb')
        for chunck in res.iter_content(100000):
            image_file.write(chunck)
        image_file.close()

    # Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done.')
