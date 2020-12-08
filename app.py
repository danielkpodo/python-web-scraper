import requests
from bs4 import BeautifulSoup


res = requests.get("https://news.ycombinator.com/")
data = res.text

soup = BeautifulSoup(data, "html.parser")

post_title = soup.select('.storylink')
post_votes = soup.select(".score")

article_headings = []
article_votes = []
for article in post_title:
    article_headings.extend(article.contents)

for vote in post_votes:
    article_votes.extend(vote.contents)

post_summary = []
for i, title in enumerate(article_headings):
    for j, score in enumerate(article_votes):
        if i == j:
            post_summary.append((title, score))


for item in post_summary:
    print(item[0], item[1])
    print("-" * 50)
