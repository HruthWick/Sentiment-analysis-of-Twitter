from textblob import TextBlob
import tweepy

keys = open(r"D:\college stuff\Project\Twitter\keys.txt", "r").read().splitlines()

api_key = keys[0]
api_key_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

term = 'BMW'
tweet_amt = 5

tweets = api.search_tweets(q=term, lang='en', tweet_mode='extended', count=tweet_amt)

polarity = 0

for tweet in tweets:
    if 'retweeted_status' in tweet._json:
        text = tweet._json['retweeted_status']['full_text']
    else:
        text = tweet.full_text
    analysis = TextBlob(text)
    polarity += analysis.polarity

print(polarity)
