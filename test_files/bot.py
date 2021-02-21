import tweepy

# API Keys
consumer_key = ""
consumer_secret = ""

key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
api.update_status("")

# Returns all mentions in bot timeline
tweets = api.mentions_timeline()
print(tweets)

