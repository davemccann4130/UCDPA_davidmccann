import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# import scraped tweets into Dataframe
df = pd.read_csv('HappinessRpttweets.csv')


df['Datetime'] = pd.to_datetime(df['Datetime'], format = '%Y-%m-%d')
#print(df.head())

tweets_line = df[['Datetime','Likecount','Retweetcount','Replycount','Quotecount']].sort_values(by='Datetime')
tweets_line = tweets_line.set_index('Datetime')

# set up the plot
#https://pythonprogramming.net/styles-matplotlib-tutorial/
matplotlib.style.use('fivethirtyeight')
sns.lineplot( data=tweets_line,  dashes = False, alpha=0.7).set_title('@HappinessRpt Twitter Engagement')

plt.xlabel('Year')
plt.ylabel('Count')
#print(plt.style.available)
plt.tight_layout()
plt.show()




