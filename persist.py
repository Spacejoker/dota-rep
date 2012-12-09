from model import *
from pymongo import Connection

class Database():

    def __init__(self):
        print 'initializing db connection'
        con = Connection()
        self.db = con.dota_search
        self.players_ = self.db.players

    def save_player(self, player):
        p = {   'name' : player.name,
                'page_url' : player.page_url}
        print 'Saving player to db: ' + str(p)
        already_in = self.players_.find({'name':player.name})
        tmp = []
        for item in already_in:
            tmp.append(item)
        if len(tmp) > 0:
            print 'player ' + player.name + ' already in db' #TODO LOG
            return -1
        self.players_.insert(p)
        return 0

    def find_player(self, name=None):
        print 'a'
        if(name == None):
            ret = []
            c = self.players_.find()
            for p in c:
                ret.append(p)
            return ret
        print 'b'
        ret = self.players_.find({'name':name})
        r = []
        for item in ret:
            r.append(item)
        return r

    def remove_player(self, name=None):
        self.players_.remove({'name':name}, safe=True)
