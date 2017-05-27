# stockyweb.py
# tch-datasci
# 05-26-2017
#
# This program is to scrape data from stock news and
# discussion sites.

import sqlite3
import urllib
import ssl
from urlparse import urljoin
from urlparse import urlparse
from BeautifulSoup import *
