import unittest
import sys
sys.path.append('../')
from model import *
from scrape import *
from persist import *

html = '<td class="cell-xlarge"><a href="/players/90892194">DK.longdd</a><i class="symbol-icon symbol-verified icon-ok" rel="tooltip" title="This player is verified as DK.longdd"></i></td>'

class TestUrlFunctions(unittest.TestCase):
    def set_up(self):
       print "nothing" 

    def test_trivial(self):
        self.assertEqual(1,1)

    def test_create_player(self):
        player = make_player_from_link(html)
        self.assertIsNotNone(player)
        self.assertEqual("DK.longdd", player.name)
        self.assertEqual("/players/90892194", player.page_url)

    def test_generate_player_list(self):
        players = generate_player_list([html])
        self.assertEqual(len(players), 1)

class TestPersistance(unittest.TestCase):

    def setUp(self):
        self.db = Database()

    def test_save_and_delete(self):
        player = Player(name="Jens", page_url="My_super_url")
        self.assertEqual(self.db.save_player(player), 0)
        self.assertEqual(self.db.save_player(player), -1)
        
        p2 = self.db.find_player(name="Jens")
        self.assertTrue(len(p2)>=1)
        self.db.remove_player(name="Jens")
        p2 = self.db.find_player(name="Jens")
        self.assertEqual(len(p2),0)
        

if __name__ == '__main__':
    unittest.main()
