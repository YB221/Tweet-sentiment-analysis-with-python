import matplotlib.pyplot as plt
import tweepy
from textblob import TextBlob
P=0
Ne=0
Nu=0
consumer_key = '4vYLAmtRXFVc9dp7s2iuuOOID'
consumer_key_secret='770qat6wInRcaV8AytlEeoJCluudAHECtFo7QsfebVW8ZG5zKM'
access_token = '2476790046-IFCtG5p5uhyIqLn19JjGoXTLmIs5yApgIKSdcMU'
access_token_secret = 'vPGih9SaGE4twxp9ZtpoWMLYAP7rvYRFHaHhIYkhi7HGk'
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
s=raw_input('what do you want to analyze?it can be a #Tag,companay,celebrity etc.\n')
co=input('how much tweets do you want to analyze?\n')
#public_tweets = api.search('#MeToo')
c=0
for tweet in tweepy.Cursor(api.search,
                           q = s,count=co,
                           lang = "en").items(co):   
     print(tweet.text)
     analysis = TextBlob(tweet.text)
     print(analysis.sentiment)
     if analysis.sentiment[0]>0:
      print( 'Positive')
      P=P+1
      c=c+1
     elif analysis.sentiment[0]<0:
      print( 'Negative')
      Ne=Ne+1
      c=c+1
     else:
      c=c+1
      print ('Neutral')
      Nu=Nu+1 
print(c)
Z=[P,Ne,Nu]  
L=['positive','negetive','neutral']     
plt.pie(Z , labels=L)
plt.axis('equal')
plt.show()
