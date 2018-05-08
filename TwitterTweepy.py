import tweepy
import json
import time

consumer_key = "k08TTiz73ZvuojkwFEQkpLEYg"
consumer_secret = "Cw8s6lDHwwIdADA6iyrgttNflnGqfqRItxUyFD5Ol371Iw328Q"

access_token = "916904657473204224-LoEweYcjafIrNo6lRAl9fBuYvIfEkWY"
access_token_secret = "eTrv0YAy516MNJ5DQfi8cvazMTePWOdEGao5Zc6SdIOOo"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

query = "TakeTheKnee"
tweets_count = 30

downloaded_tweets = [];
last_id = -1;


while(len(downloaded_tweets) < tweets_count):
    count = tweets_count - len(downloaded_tweets)
    try:
        new_tweet = api.search(query, lang="en", count = count , max_id = str(last_id-1))
        if not new_tweet:
            break;
        for tweet in new_tweet:
            downloaded_tweets.append(tweet._json)
        last_id = new_tweet[-1].id;
    except tweepy.TweepError as e:
        print("Downloaded tweets %s"%(len(downloaded_tweets)));
        print("now going to sleep")
        time.sleep(60 * 15)
        print("Woke up")
        continue
    except StopIteration:
        break

with open("/Users/KrishnChinya/PycharmProjects/Twitter/Tweets.json", mode='w', encoding='utf-8') as jsonfile:
    json.dump(downloaded_tweets, jsonfile)
