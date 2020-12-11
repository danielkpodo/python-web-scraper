import requests
from bs4 import BeautifulSoup
import pprint
import csv

res = requests.get("https://coreyms.com/")
data = res.text

soup = BeautifulSoup(data, "html.parser")

titles = soup.select('.entry-title a')
date_published = soup.select(".entry-time")
article_summary = soup.select(".entry-content p")


# print(titles)

posts = []

for i, title in enumerate(titles):
    link = title.get('href')
    title = title.get_text()
    post_summary = article_summary[i].get_text()
    posts.append({"Title": title, "URL Link": link,
                  "Content Summary": post_summary})


# pprint.pprint(posts)
fields = ["Title", "URL Link", "Content Summary"]
try:
    with open('./posts.csv', mode='w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
        csv_writer.writeheader()
        csv_writer.writerows(posts)

except FileNotFoundError as err:
    print("Missing file: ", err)

else:
    print("Csv of posts has been created successfully")
