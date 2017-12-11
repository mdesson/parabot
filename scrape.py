from urllib import request
from bs4 import BeautifulSoup
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
hoi4_rss = request.Request("https://forum.paradoxplaza.com/forum/index.php?forums/hearts-of-iron-iv.844/index.rss", headers=headers)

def make_soup(url):
    """Generates soup object with given url."""
    res = request.urlopen(url)
    html = res.read()
    soup = BeautifulSoup(html, "lxml")
    return soup

soup_rss = make_soup(hoi4_rss)
posts = soup_rss.find_all("a")

for i in posts:
    if "hoi4 dev diary - " in str(i).lower():
        thread_url = re.search(r"https.*?(?=\")", str(i)).group()

print(thread_url)

soup_diary = make_soup(thread_url)
