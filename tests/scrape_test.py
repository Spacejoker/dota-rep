import unittest
import sys
sys.path.append('../')
from model import *
from scrape import *
from persist import *

#he only plays wisp so this one should work a while at least
class TestPlayerInfo(unittest.TestCase):
    @unittest.skip("")
    def test_most_used_heroes(self):
        player = scrape_player_by_url('/players/85805514/_heroes')
        print player.top_heroes[0]
        self.assertEqual(player.top_heroes[0].name, "Wisp")

#time consuming, arund 5 seconds
class TestIntegration(unittest.TestCase):

    @unittest.skip("")
    def test_generate_players(self):
        players = scrape_player_page(1)
        #self.assertEqual(len(players), 81)

    @unittest.skip ("")
    def test_full_call(self):
        players = gen_full_player_list()
        #self.assertEqual(len(players), 80)
        for p in players:
            self.assertIsNotNone(p.name)
            self.assertIsNotNone(p.page_url)


class TestGetPlayerGames(unittest.TestCase):

    def test_get_some(self):
       ret = get_latest_games() 
       self.assertIsNotNone(ret)
       self.assertTrue(len(ret) > 0, "no hits")


if __name__ == '__main__':
    unittest.main()
