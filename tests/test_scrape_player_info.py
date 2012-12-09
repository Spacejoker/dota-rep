import unittest
import sys
sys.path.append('../')
from model import *
from scrape import *
from persist import *

class TestPlayerInfo(unittest.TestCase):
    def test_most_used_heroes(self):
        player = scrape_player_by_url('/players/85805514/_heroes')
        print player.top_heroes[0]
        self.assertEqual(player.top_heroes[0].name, "Wisp")

if __name__ == '__main__':
    unittest.main()
