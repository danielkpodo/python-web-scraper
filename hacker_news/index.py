import requests
from bs4 import BeautifulSoup
import pprint
# *********** HACKER NEWS *********** #

res = requests.get("https://news.ycombinator.com/")
data = res.text

soup = BeautifulSoup(data, "html.parser")

links = soup.select('.storylink')
votes = soup.select(".score")


def get_hacker_news_content(links, votes):
    posts = []
    for i, link in enumerate(links):
        for j, vote in enumerate(votes):
            if i == j:
                title = link.get_text()
                href = link.get('href')
                score = int(vote.get_text().replace(" points", ""))
                if score > 100:
                    posts.append(
                        {"title": title, "href": href, "score": score})
    return posts


posts = get_hacker_news_content(links, votes)
# print(get_hacker_news_content(links, votes))

# Sorting by votes descending
sorted_posts = sorted(posts, key=lambda x: x.get('score'), reverse=True)
pprint.pprint(sorted_posts)
