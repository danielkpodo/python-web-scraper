import requests
from bs4 import BeautifulSoup
import pprint
# *********** HACKER NEWS *********** #
current_page = 1
pages_to_get = 2

mega_links = []
mega_votes = []

while (current_page <= pages_to_get):
    res = requests.get(f"https://news.ycombinator.com/news?p={current_page}")
    current_page += 1
    data = res.text

    soup = BeautifulSoup(data, "html.parser")

    links = soup.select('.storylink')
    votes = soup.select(".score")

    mega_links.extend(links)
    mega_votes.extend(votes)


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


posts = get_hacker_news_content(mega_links, mega_votes)

# Sorting by votes descending
sorted_posts = sorted(posts, key=lambda x: x.get('score'), reverse=True)
# pprint.pprint(sorted_posts)
print("Sorted Posts", len(sorted_posts))
print("Mega Votes", len(mega_votes))
print("Mega Links", len(mega_links))
