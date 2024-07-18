# from twitter_scraper.modules import tweets
from twitterpeel import get_tweets
# from twitter_scraper.modules import *
# a=tweets.get_tweets('iamsrk')
# b=Profile('iamsrk')
# b.to_dict()
# print(b)
for tweet in get_tweets('twitter', pages=1):
     print(tweet['text'])