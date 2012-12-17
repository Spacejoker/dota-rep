import urllib2
from bs4 import BeautifulSoup
import re
from model import *
from scrape import *
import urllib

def parse():
    soup = read_url('https://dotabuff.com/heroes')
    hero_links = soup.findAll(attrs={"class":"tile-container tile-container-hero"})
    hero_list = ''
    f = open('herolist.txt','w')
    
    hero_name_parts = img_url.split('/')[-1].split('-')[:-1]
    hero_name = ''
        for part in hero_name_parts:
            hero_name += part + '_'
        hero_name = hero_name[:-1]
        hero_list.append(Hero(hero_name, hero_name + '.png'))
        urllib.urlretrieve(img_url, 'static/' + hero_name + '.png')
        print 'deluxe'
    f.close() 

if __name__=='__main__':
    parse()
