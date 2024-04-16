import tweepy

# Replace 'your...' with your actual keys and tokens
consumer_key = 'Hf2vf21dl6udXOa5MO1f84dps'
consumer_secret = 'jFt37k5pe04bcwONUEb5BPkrz4wXMmZ4Kh2DkxIWp1BIm99GhB'
access_token = '1328482358044012544-42sqS3NIBTlOoGWuu17la9thSFwkUR'
access_token_secret = '6WZJZHk0nD6iapYMFYFA6OdIZghzx61UTI76mrqSGPpUh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

import pandas as pd

# Define your search query and how many tweets you want per issue
search_queries = ['Abortion', 'Gun Control', 'Immigration Healthcare', ...]  # Complete this list
tweets_per_issue = 30  # Number of tweets you want to pull per issue

# Container for all tweets
all_tweets = []

for query in search_queries:
    tweets = api.search_tweets(q=query + " -filter:retweets", lang="en", count=tweets_per_issue)
    for tweet in tweets:
        all_tweets.append({
            'text': tweet.text,
            'created_at': tweet.created_at,
            'likes': tweet.favorite_count,
            'retweets': tweet.retweet_count,
            'user_followers': tweet.user.followers_count
        })

# Convert to DataFrame
df_tweets = pd.DataFrame(all_tweets)
