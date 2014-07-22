minus_context
=============
Minus Context by @natematias and @smwat, inspired by @NYTMinusContext on Twitter, downloads all content from an RSS feed and tweets out a random sentence from that feed.

To install:

1. set up the following Python modules:
```
sudo pip install nltk feedparser HTMLParser twitter yaml
```

2. Copy config.yaml.sample to config.yaml and add your Twitter app's credentials
3. Change the RSS feed in tweet_minus_context.py to the feed you want to monitor
4. To tweet, run 
```
python tweet_minus_context.py
```

Let us know what Twitter accounts you create!
