import requests
from bs4 import BeautifulSoup

res = requests.get("https://able.bio/rhett")
data = res.text

soup = BeautifulSoup(data, "html.parser")

# passing the page skeleton to the beautiful soup function gives a beautiful soup object
title = soup.title
# print(title.name)  # gives you the name of the tag
# print(title.parent.name)

# get all links from a webpage
for link in soup.findAll('a'):
    print(link.get('href'))

# get text content
print(title.get_text())

article = soup.select('.article-card')

print(article)
