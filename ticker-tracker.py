# ticker-tracker.py
# tch-datasci
# 05-26-2017
#
# This program is to clean and sort data scraped from
# stock news and discussion sites. It is meant to create
# a database of company names, their stock ticker symbols
# and the exchange their stocks are traded on.

import sqlite3
import re

conn = sqlite3.connect('stockydb.sqlite')
crsr = conn.cursor()

crsr.execute('''CREATE TABLE IF NOT EXISTS Companies (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    ticker TEXT UNIQUE,
    exchange TEXT
)''')
