import matplotlib.pyplot as plt
import tweepy
from textblob import TextBlob
P=0
Ne=0
Nu=0
consumer_key = 'cO4PJdfaFSvX25BB7ysQio7Q2'
consumer_key_secret='31REzY4Q8NRZuqQxlwCtBcgZZeqZyLiClxEyAoerhX6M91TfUb'
access_token = '2476790046-ueMP4B4lfaxkNgKpcqcdxlFAW5ZpTQuXE3dEfX1'
access_token_secret = 'iA1pKvofwVpbzhgtUyGQY9glulVn8mqzryoPRbIk0Csbk'
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search('#metoo')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
      print( 'Positive')
      P=P+1
    elif analysis.sentiment[0]<0:
      print( 'Negative')
      Ne=Ne+1
    else:
      print ('Neutral')
      Nu=Nu+1 

Z=[P,Ne,Nu]  
L=['positive','negetive','neutral']     
plt.pie(Z , labels=L)
plt.show()
