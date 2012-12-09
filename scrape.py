import urllib2
from bs4 import BeautifulSoup
import re
from model import *

def gen_full_player_list():
    ret = []
    for page_nr in range(1,5):
        ret.extend(scrape_player_page(page_nr))
    return ret

def scrape_player_page(pagenr=1):
    url = 'https://dotabuff.com/players/verified?page=' + str(pagenr)
    raw_html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(raw_html)

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


