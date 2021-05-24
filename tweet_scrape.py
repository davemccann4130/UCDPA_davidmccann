# https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af
# need to install the developer version of snscrape in order for this to work
# pip install --trusted-host pypi.python.org git+https://github.com/JustAnotherArchivist/snscrape.git#egg=snscrape
# has a limitation in that it can only be run once every 24 hours - twitter refuses the request on second attempt

import snscrape.modules.twitter as sntwitter
import pandas as pd
#import time

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:HappinessRpt').get_items()):
    #time.sleep(1)
    if i > 1000:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.likeCount,
                         tweet.retweetCount, tweet.replyCount, tweet.quoteCount])

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet_Id', 'Text', 'Username',
                                                 'Likecount', 'Retweetcount', 'Replycount', 'Quotecount'])
username = tweets_df1.at[1, 'Username']
tweets_df1.to_csv(username+'tweets.csv')

print(tweets_df1.head())
#print(tweets_df1.info())
#print(tweets_df1.describe())
#print(tweets_df1.shape)
#print(tweets_df1.values)
#print(tweets_df1.columns)
#print(tweets_df1.index)
#print(len(tweets_df1))

#print(tweets_df1[['Username', 'Tweet Id','Datetime','Text' ]].head())


