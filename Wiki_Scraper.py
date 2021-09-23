from bs4 import BeautifulSoup
from random import shuffle
import requests
def random_wiki_scraper(url):
    r=requests.get(url=url)
    content=r.content
    soup=BeautifulSoup(content,'html.parser')
    print(soup.find(id="firstHeading").text)
    link_list=soup.find(id='bodyContent')find_all('a')
    shuffle(link_list)
    link_to_scrape=0
    for link in link_list:
        if link.get('href').find("/wiki/")==-1:
            continue
        link_to_scrape=link
        break
    random_wiki_scraper("https://en.wikipedia.org"+link_to_scrape['href'])
random_wiki_scraper('https://en.wikipedia.org/wiki/Web_scraping')
        