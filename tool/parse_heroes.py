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
    for link in hero_links:
        img_link = str(link['style']).split('url')[1][1:-1]
        img_url = 'https://dotabuff.com/' + img_link
        hero_name = img_url.split('/')[-1].split('-')[0]
        f.write(hero_name + '\n')
        #urllib.urlretrieve(img_url, 'static/' + hero_name + '.png')
    f.close()
if __name__=='__main__':
    parse()
