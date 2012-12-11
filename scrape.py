import urllib2
from bs4 import BeautifulSoup
import re
from model import *

root_domain = 'https://dotabuff.com'

def read_url(url):
    return BeautifulSoup(urllib2.urlopen(url).read())

def gen_full_player_list():
    ret = []
    for page_nr in range(1,5):
        ret.extend(scrape_player_page(page_nr))
    return ret

def scrape_player_page(pagenr=1):
    url = root_domain + '/players/verified?page=' + str(pagenr)
    soup = read_url(url)#{urllib2.urlopen(url).read()

    players = soup.findAll(attrs={"class":"cell-xlarge"})
    
    return generate_player_list(players)

def generate_player_list(url_list):
    ret = []

    for p in url_list:
        ret.append(make_player_from_link(str(p)))

    return ret

def make_player_from_link(link):
    soup = BeautifulSoup(link) 
    a = soup.find('a')
    name = a.text
    page_url = a['href']
    return Player(name=name, page_url=page_url)

def scrape_player_by_url(url_extension):
    
    url = root_domain + url_extension 
    print url.split("</a>")
    soup = read_url(url)#hrllib2.urlopen(url).read()
    print soup
    heroes = soup.findAll(attrs={"id":"page-content"})

    #for item in str(soup).split("</a>"):
    #    print item
    print heroes
    return PlayerDetails([Hero('Pugna')])
