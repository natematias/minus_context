import nltk
import feedburner
import random
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
 
# download a feed
feed_url = "http://feeds.feedburner.com/saramwatson"
feed = feedburner.parse(feed_url)

posts = [strip_tags(x['summary']) for x in feed['entries']]
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

sentences = []

for post in posts:
  for sentence in sent_detector.tokenize(post.strip()):
    if len(sentence) <=140:
      sentences.append(sentence)

print(random.choice(sentences))
