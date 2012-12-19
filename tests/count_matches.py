import unittest
import sys
sys.path.append('../')
from scrape import *
from persist import *

class TestMongo(unittest.TestCase):

    def setUp(self):
        self.db = Database()

    def test_get_some(self):
        self.db.remove_match()
        self.db.save_match({u'heroes': [{u'player': u'daniel.l...', u'hero': u'Ogre Magi'}, {u'player': u'fnysboda', u'hero': u'Lina'}, {u'player': u'safeyoda', u'hero': u'Brewmaster'}, {u'player': u'wrftw', u'hero': u'Timbersaw'}, {u'player': u'blacksmoke', u'hero': u'Bounty Hunter'}, {u'player': u'Fancybunny', u'hero': u'Luna'}, {u'player': u'toxicFork', u'hero': u'Phantom Lancer'}, {u'player': u'DotAholi...', u'hero': u'Drow Ranger'}, {u'player': u'Flash_ot', u'hero': u'Lifestealer'}, {u'player': u'DotAholi...', u'hero': u'Weaver'}], u'type': u'match', u'match_id': u'Match 79804452', 'summary': 'The summary'})
        self.db.save_match({u'heroes': [{u'player': u'daniel.l...', u'hero': u'Ogre Magi'}, {u'player': u'fnysboda', u'hero': u'Lina'}, {u'player': u'safeyoda', u'hero': u'Brewmaster'}, {u'player': u'wrftw', u'hero': u'Timbersaw'}, {u'player': u'blacksmoke', u'hero': u'Bounty Hunter'}, {u'player': u'Fancybunny', u'hero': u'Luna'}, {u'player': u'toxicFork', u'hero': u'Phantom Lancer'}, {u'player': u'DotAholi...', u'hero': u'Drow Ranger'}, {u'player': u'Flash_ot', u'hero': u'Lifestealer'}, {u'player': u'DotAholi...', u'hero': u'Weaver'}], u'type': u'match', u'match_id': u'Match abc12379804452', 'summary': 'The summary'})
        match_cnt = self.db.count_matches()
        self.assertEqual(match_cnt, 2)

if __name__ == '__main__':
    unittest.main()
