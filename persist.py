from model import *
from pymongo import Connection

class Database():

    def __init__(self):
        con = Connection()
        self.db = con.dota_search
        self.players_ = db.players

    def save_player(self, player):
        p = {   "name" : player.name,
                "page_url" : player.page_url}
        self.players_.insert(p)

    def find_player(self, name=None):
        return self.players_.find({"name":name})

    def remove_player(self, name=None):
        self.players_.remove({"name":name})
