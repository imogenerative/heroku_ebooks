import os

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

SOURCE_ACCOUNT = os.environ['SOURCE_ACCOUNT']
ODDS = int(os.environ['ODDS'])
ORDER = int(os.environ['ORDER'])
SOURCE_EXCLUDE = os.environ['SOURCE_EXCLUDE']

TWEET_ACCOUNT = os.environ['TWEET_ACCOUNT']

DEBUG = False
STATIC_TEST = False
SCRAPE_URL = False
