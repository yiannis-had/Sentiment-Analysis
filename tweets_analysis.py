from textblob import TextBlob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def analyze_polarity(tweet):
    analysis = TextBlob(tweet)
    pol = round(analysis.sentiment.polarity, 3)
    return pol


df = pd.read_fwf('friday23-11.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
df['polarity'] = np.array([analyze_polarity(tweet) for tweet in df['Tweets']])
df2 = pd.read_fwf('saturday24-11.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
df2['polarity'] = np.array([analyze_polarity(tweet) for tweet in df2['Tweets']])
df3 = pd.read_fwf('sunday25-11.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
df3['polarity'] = np.array([analyze_polarity(tweet) for tweet in df3['Tweets']])
df4 = pd.read_fwf('monday26-11.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
df4['polarity'] = np.array([analyze_polarity(tweet) for tweet in df4['Tweets']])
df5 = pd.read_fwf('tuesday27-11.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
df5['polarity'] = np.array([analyze_polarity(tweet) for tweet in df5['Tweets']])
# df6 = pd.read_fwf('sunday13-1.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
# df6['polarity'] = np.array([analyze_polarity(tweet) for tweet in df6["Tweets"]])
# df7 = pd.read_fwf('monday14-1.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
# df7['polarity'] = np.array([analyze_polarity(tweet) for tweet in df7["Tweets"]])
# df8 = pd.read_fwf('tuesday15-1.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
# df8['polarity'] = np.array([analyze_polarity(tweet) for tweet in df8["Tweets"]])
# df9 = pd.read_fwf('wednesday16-1.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
# df9['polarity'] = np.array([analyze_polarity(tweet) for tweet in df9["Tweets"]])
# df10 = pd.read_fwf('thursday17-1.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
# df10['polarity'] = np.array([analyze_polarity(tweet) for tweet in df10["Tweets"]])

# df6['MA'] = df6['polarity'].rolling(window=250, min_periods=2).mean()
# polarity = pd.Series(data=df6['polarity'].values)
# polarity.plot(figsize=(16, 4))
# ma = pd.Series(data=df6['MA'].values)
# ma.plot(figsize=(16, 4))
# plt.title("Sentiment scores for Sunday 13th of January 2019")
# plt.show()


# Means
# df  0.0450223523150612
# df2 0.04026940247252747
# df3 0.037034884532198414
# df4 0.07016615698267074
# df5 0.041824836390078377
# df6 0.04981193508627774
# df7 0.05163466042154567
# df8 0.057370654535578484
# df9 0.06657062563869648
# df10 0.058768808718526876

# friday = pd.Series(data=df['polarity'].values)
# friday.plot(figsize=(16, 4))
# plt.show()
# saturday = pd.Series(data=df2['polarity'].values)
# saturday.plot(figsize=(16, 4))
# plt.show()
# sunday = pd.Series(data=df3['polarity'].values)
# sunday.plot(figsize=(16, 4))
# plt.show()
# monday = pd.Series(data=df4['polarity'].values)
# monday.plot(figsize=(16, 4))
# plt.show()
# monday = pd.Series(data=df5['polarity'].values)
# monday.plot(figsize=(16, 4))
# plt.show()

