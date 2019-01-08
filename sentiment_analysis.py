import matplotlib.pyplot as plt #importing the data ploting library
import re #text filtering library
import tweepy   #importing the tweet fetching library
from textblob import TextBlob #importing the anlysis performing library 
P=0  #counter for positive tweets
Ne=0 #counter for negetive tweets
Nu=0 #counter for neutral tweets
#saving variables so that code dose'nt seem to be written in gibberish :) 
consumer_key = '4vYLAmtRXFVc9dp7s2iuuOOID' 
consumer_key_secret='770qat6wInRcaV8AytlEeoJCluudAHECtFo7QsfebVW8ZG5zKM'
access_token = '2476790046-IFCtG5p5uhyIqLn19JjGoXTLmIs5yApgIKSdcMU'
access_token_secret = 'vPGih9SaGE4twxp9ZtpoWMLYAP7rvYRFHaHhIYkhi7HGk'
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret) # authenticating with twitter API
auth.set_access_token(access_token, access_token_secret) # reaching to our app that we created in twitter API
api = tweepy.API(auth)
s=raw_input('what do you want to analyze?it can be a #Tag,companay,celebrity etc.\n')
co=input('how much tweets do you want to analyze?\n')
c=0
for tweet in tweepy.Cursor(api.search,                      #using cursor in tweepy to get tweets it automatically takes care of 'pagination'
                           q = s,count=co,
                           lang = "en",tweet_mode='extended').items(co):
     nova=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)|(https\S+)", " ", tweet.full_text)#removing links and stuff that may affect analysis but isn't needed.NOTE:retweets will not be shown in extended mode neither their links will be removed by this.ping me if you can help!!!
     print(nova) #printing what we've extracted
     analysis = TextBlob(nova) #analysisng what we've printed
     print(analysis.sentiment)#printing what we've analysed in mathematical or technical tems.
    #printing what we've analysed in layman's terms
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
#ploting a fancy pie chart of out analysis.
Z=[P,Ne,Nu]  
L=['positive','negetive','neutral']     
plt.pie(Z , labels=L)
plt.axis('equal')
plt.show()
