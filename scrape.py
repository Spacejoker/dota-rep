import urllib2
from bs4 import BeautifulSoup
import re
from model import *
import urllib

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
    soup = read_url(url)#hrllib2.urlopen(url).read()
    heroes = soup.findAll(attrs={"id":"page-content"})

    return PlayerDetails([Hero('Pugna')])

def refresh_heroes(db):
    db_heroes = db.find_hero()
    web_heroes = parse_current_heroes()

    new_heroes = []

    for wh in web_heroes:
        found = False
        for dh in db_heroes:
            if dh.name == wh.name:
                found = True
        if not found:
            new_heroes.append(wh)
    
    for h in new_heroes:
        db.save_hero(h)

    return new_heroes

def parse_current_heroes(save_img=False):
    soup = read_url('https://dotabuff.com/heroes')
    hero_links = soup.findAll(attrs={"class":"tile-container tile-container-hero"})
    hero_list = []
   
    for link in hero_links:
        img_link = str(link['style']).split('url')[1][1:-1]
        img_url = 'https://dotabuff.com/' + img_link
        hero_name_parts = img_url.split('/')[-1].split('-')[:-1]
        hero_name = ''
        for part in hero_name_parts:
            hero_name += part + '_'
        hero_name = hero_name[:-1]
        hero_list.append(Hero(hero_name, hero_name + '.png'))
        if save_img:
            urllib.urlretrieve(img_url, '../static/hero_img/' + hero_name + '.png')
         
    return hero_list

def get_latest_games(player_id='67601693'):
    url = 'https://dotabuff.com/players/' + player_id + '/matches'
    soup = read_url(url)
    tbody = soup.findAll('tbody')[0]
    ret = []
    for row in tbody:
        links = row.findAll('a')
        match_id = links[1]['href']
        
        match_id = match_id.split('/')[2]
        match_info = {'main_hero' :  links[1].text, 'match_id' : match_id}
        ret.append({ 'data' : match_info})
    return ret 


def add_match(match_id='', db=None):
    print 'scraping match ' + match_id
    soup = read_url('https://dotabuff.com/matches/' + match_id)

    tbodies = soup.findAll('tbody')
    ret = {'type' : 'match'}
    hero_data = []
    for tbody in tbodies:
        for row in tbody:
            tmp = {}
            links = row.findAll('a')
            tmp['player'] = links[1].text
            tmp['hero'] = links[3].text
            tmp['k'] = row.findAll('td')[4].text
            tmp['d'] = row.findAll('td')[5].text
            tmp['a'] = row.findAll('td')[6].text
            hero_data.append(tmp)
    
    ret['heroes'] = hero_data    
    ret['match_id'] = soup.find('h1').text
    db.save_match(ret)

def scrape_player(player_id, db):
    print player_id
    url = 'https://dotabuff.com/players/' + player_id + '/matches'
    print url
    soup = read_url(url)
    links = soup.findAll(attrs={'class':'matchid'})#attrs={'class':'hero-link'})#[].findAll('tr')
    for link in links:
        add_match(link.text, db)
    
