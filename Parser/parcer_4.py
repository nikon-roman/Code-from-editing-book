import tweepy


consumer_key = "<Приховано>"
consumer_secret = "< Приховано >"
access_token = "< Приховано >"
access_token_secret = "< Приховано>"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

status = api.update_status(status="Hello, World!")
