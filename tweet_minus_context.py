import nltk
import feedparser
import random
from HTMLParser import HTMLParser
import twitter
import yaml

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(post):
    if 'content' in post:
      html = post['content']
    elif 'summary' in post:
      html = post['summary']
    else:
      html =""
    try:
      s = MLStripper()
      s.feed(html)
      return s.get_data()
    except:
      return ""
 
# download a feed from Berkman Planet
feed_url = "http://cyber.law.harvard.edu/planet/current/atom.xml"
feed = feedparser.parse(feed_url)

# create a list of posts
posts = [strip_tags(x) for x in feed['entries']]

#load sentence tokenizer
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

sentences = []

#for each post and each tweet length sentence, add to candidates9
for post in posts:
  for sentence in sent_detector.tokenize(post.strip()):
    if len(sentence) <=140 and len(sentence) > 50:
      sentences.append(sentence)

api_key = yaml.load(open('config.yaml'))

api = twitter.Api(consumer_key=api_key['api'],
  consumer_secret=api_key['consumer_secret'],
  access_token_key=api_key['access_token_key'],
  access_token_secret=api_key['access_token_secret'])

# Tweet out a random sentence
tweet = random.choice(sentences)
print tweet
api.PostUpdate(tweet)
