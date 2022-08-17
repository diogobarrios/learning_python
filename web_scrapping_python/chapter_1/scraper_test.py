from urllib.request import urlopen

# Open the html page and save into a variable
html = urlopen("http://pythonscraping.com/pages/page1.html")
# Call the method .read() to read the html info from variable html
print(html.read())