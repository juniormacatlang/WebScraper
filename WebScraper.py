#   Web Scraper
#   Rommel D. Macatlang Jr.

from bs4 import BeautifulSoup
from urllib.request import urlopen



url = input("Enter Website URL: ") #http://books.toscrape.com/
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

#print(html) #Use to find the HTML tags desired

soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())

