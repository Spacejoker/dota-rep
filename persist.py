from model import *
from pymongo import Connection
import os
if 'MONGOHQ_URL' in os.environ:
    url = urlparse(os.environ['MONGOHQ_URL'])
    DB = url.path[1:]
    DB_HOST = url.hostname
    DB_PORT = url.port
    DB_USER = url.username
    DB_PASS = url.password

class Database():

    def __init__(self):
        print 'initializing db connection'
        conn = connect(settings.DB, host=settings.DB_HOST, port=settings.DB_PORT, username=settings.DB_USER, password=settings.DB_PASS)
        db = conn[settings.DB]
        db.authenticate(settings.DB_USER, settings.DB_PASS)
        self.db = db
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
