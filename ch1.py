import requests
import feedparser
import json

url = f'https://www.theverge.com/rss/index.xml'
r= requests.get(url)

if r.status_code != 200:
    print(f"error with status code {r.status_code}")

#los primeros 10 items

feed = feedparser.parse(url)

items = feed.entries[:10]

for i, item in enumerate(items, start=1):
    title = item.title
    pub_date = item.published
    link = item.link

    print(f"{i}. Title: {title}")
    print(f"Date: {pub_date}")
    print(f"Link: {link}")

 #Guardar un archivo JSON
data = []
for item in items:
    lista = {
        "title": item.title,
        "published": item.published,
        "link": item.link
    }
    data.append(lista)


with open("10items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

