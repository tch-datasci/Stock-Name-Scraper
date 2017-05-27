import sqlite3
import json
import urllib
import re

conn = sqlite3.connect('tickerdb.sqlite')
crsr = conn.cursor()

crsr.execute('''
DROP TABLE IF EXISTS Companies''')

crsr.execute('''

CREATE TABLE Companies (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    ticker TEXT UNIQUE,
    exchange TEXT
);

''')
