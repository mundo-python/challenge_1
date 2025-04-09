import requests
from bs4 import BeautifulSoup 

url = f'https://www.theverge.com/rss/index.xml'
r= requests.get(url)


soup = BeautifulSoup(r.text, 'lxml')
#print(soup)

items = soup.find_all("item", limit = 10)

for item in items:
    title = item.title.text 
    pub_date = item.pubDate.text 
    link = item.link.text
    print(f"Title: {title}")
    print(f"Date: {pub_date}")
    print(f"Link: {link}")

