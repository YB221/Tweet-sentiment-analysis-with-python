import tweepy
from textblob import TextBlob
consumer_key='foo'
consumer_key_secret='foo'
access_token='foo' 
access_token_secret='foo'
auth=tweepy.OAuthHandler(consumer_key,consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)
public_tweets=api.search('#metoo')
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
       print( 'Positive')
    elif analysis.sentiment[0]<0:
       print( 'Negative')
    else:
       print ('Neutral')
