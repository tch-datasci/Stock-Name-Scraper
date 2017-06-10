# stockyweb.py
# tch-datasci
# 05-26-2017
#
# This program is to scrape data from reddit and store them to eventually
# be used to find "meme stocks"

import sqlite3
import urllib
from BeautifulSoup import *
import praw

# Connect to the sqlite db
conn = sqlite3.connect(stockydb.sqlite)
crsr = conn.cursor()

#if the table isnt there, create it.
crsr.execute('''CREATE TABLE IF NOT EXISTS Raw (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    URL TEXT UNIQUE,
    HTML TEXT UNIQUE,
    ACCESSED DATE,
    POSTED DATE,
)''')

# Use Reddit's API to get info from the subreddits. Enter in your own user_agent
# client_id, client_secret, username and passwords please

reddit = praw.Reddit(user_agent='XXXX',
                     client_id='XXXX', client_secret="XXXX",
                     username='XXXX', password='XXXX')

submission = reddit.submission(id='6gev13')

for top_level_comment in submission.comments:
    print(top_level_comment.body)
