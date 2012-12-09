import unittest
import sys
sys.path.append('../')
from model import *
from scrape import *
from persist import *


class TestIntegration(unittest.TestCase):

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
