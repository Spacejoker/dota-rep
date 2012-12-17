import urllib2
import sys
sys.path.append('../')
from bs4 import BeautifulSoup
import re
from scrape import *

if __name__=='__main__':
   parse_current_heroes(True) 
