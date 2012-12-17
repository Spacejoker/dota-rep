from model import *
import pymongo 
import os
import traceback
from urlparse import urlparse

class Database():

    def __init__(self):
#        print 'initializing db connection'
        try:
            # Get a connection
            conn = pymongo.Connection(os.environ.get('MONGOHQ_URL'))
            # Get the database
            db = conn[urlparse(os.environ.get('MONGOHQ_URL')).path[1:]]
        except:
            #tb = traceback.format_exc()
            # Not on an app with the MongoHQ add-on, do some localhost action
            conn = pymongo.Connection('localhost', 27017)
            db = conn['dota']
        #get db and collections
        self.db = db
        self.players_ = self.db.players
        self.hero_ = self.db.hero

#player crud
    def save_player(self, player):
        p = {   'name' : player.name,
                'page_url' : player.page_url}
        
        already_in = self.players_.find({'name':player.name})
        tmp = []
        for item in already_in:
            tmp.append(item)
        if len(tmp) > 0:
            return -1
        self.players_.insert(p)
        return 0

    def find_player(self, name=None):
       
        if(name == None):
            ret = []
            c = self.players_.find()
            for p in c:
                ret.append(p)
            return ret
        
        ret = self.players_.find({'name':name})
        r = []
        for item in ret:
            r.append(item)
        return r

    def remove_player(self, name=None):
        self.players_.remove({'name':name}, safe=True)

#hero crud
    def save_hero(self, hero):
        h = {'type' : 'hero',
                'name' : hero.name,
                'img_link' : hero.img_link }
        self.hero_.save(h)

    def find_hero(self, name=None):
        ret = []
        c = self.hero_.find({'type':'hero'})
        for h in c:
            hero = Hero(h['name'], h['img_link'])
            ret.append(hero)
        return ret

    def remove_hero(self, name=None):
        if name==None:
            self.hero_.remove({
                'type' : 'hero'}, safe=True)
        else:
            self.hero_.remove({
                'name' : name,
                'type' : 'hero'}, safe=True)
