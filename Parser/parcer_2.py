from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://www.positive.news/").read()
soup = BeautifulSoup(html, "html.parser")
titles_elem = soup.find_all("a", {"class": "card__title"})
for title in titles_elem:
    print(title.text)
