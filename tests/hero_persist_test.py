import unittest
import sys
sys.path.append('../')
from model import *
from scrape import *
from persist import *

class TestHero(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_save_and_delete(self):
        self.db.remove_hero()
        self.db.save_hero("Alchemist", "some_url")
        res = self.db.find_hero("Alchemist")
        self.assertEqual(len(res), 1)
        
        self.db.remove_hero("Bloodseeker")
        res = self.db.find_hero("Alchemist")
        self.assertEqual(len(res), 1, "Removed alch when trying to remove bloodseeker")

        self.db.remove_hero("Alchemist")
        res = self.db.find_hero("Alchemist")
        if len(res) > 0:
            print res[0]
        self.assertEqual(len(res), 0, "Still heroes in db, should be empty")

if __name__ == '__main__':
    unittest.main()
