import unittest
import sys
sys.path.append('../')
from model import *
from scrape import *

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

    def test_generate_players(self):
        players = scrape_player_page(1)
        self.assertEqual(len(players), 25)

    def test_full_call(self):
        players = gen_full_player_list()
        self.assertEqual(len(players), 80)
        for p in players:
            self.assertIsNotNone(p.name)
            self.assertIsNotNone(p.page_url)

if __name__ == '__main__':
    unittest.main()
