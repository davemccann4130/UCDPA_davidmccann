import pandas as pd
from nltk.corpus import stopwords
import matplotlib. pyplot as plt
import seaborn as sns

# import scraped tweets into Dataframe
df = pd.read_csv('HappinessRpttweets.csv')


# split text into seperate words -- https://sigdelta.com/blog/text-analysis-in-pandas/
df['sep_words'] = df.Text.str.strip().str.split('[\W_]+')
print(df['sep_words'])

# iterrate through and create new dataframe with row for each word - https://sigdelta.com/blog/text-analysis-in-pandas/
rows = list()
for row in df[['Tweet_Id', 'sep_words']].iterrows():
    r = row[1]
    for word in r.sep_words:
        rows.append((r.Tweet_Id, word))

words = pd.DataFrame(rows, columns=['Tweet_Id', 'word'])
#print(words.to_string())


#set to lower case
words['word'] = words.word.str.lower()
#print(words.head())

#remove stopwords - https://stackoverflow.com/questions/29523254/python-remove-stop-words-from-pandas-dataframe
stop = stopwords.words('english')
words['word_no_stopwords'] = words['word'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
#print(words['word_no_stopwords'].to_string())


# create new df and remove all blank values from no stopwords column
no_stopwords =  words[['Tweet_Id','word_no_stopwords']]
#print(no_stopwords.head())
#print(type(no_stopwords))
#print(type(words))

# drop rows where stopwords were removed - stopwords removal left emptry strings rather than NaN so dropna() didnt work
tweet_words = no_stopwords[no_stopwords['word_no_stopwords'].astype(bool)]

# as the above returns a panda series, i convert to dataframe. Index causing issues plotting so added .reset_index()
tweet_words = tweet_words['word_no_stopwords'].value_counts().rename_axis('unique_words').to_frame('count').reset_index()

print(tweet_words.head())
#print(tweet_words.to_string())
print(type(tweet_words))
#print(tweet_words.index)

#https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-frequencies-in-python/
# https://seaborn.pydata.org/examples/part_whole_bars.html
# Plot horizontal bar graph

# plot from index 2 as co and https are in slots 0 and 1
tweet_words_plot = tweet_words.iloc[2:52,:]
print(tweet_words.to_string())

# plot
sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(8, 8))

sns.set_color_codes('pastel')
sns.barplot(x= 'count', y='unique_words', data=tweet_words_plot,
            label='Total',palette="viridis").set_title("Top 50 Tweeted Words - @HappinessRpt")

# Add a legend  and axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 160), ylabel="words",
       xlabel="count")
sns.despine(left=True, bottom=True)


plt.tight_layout()
plt.show()