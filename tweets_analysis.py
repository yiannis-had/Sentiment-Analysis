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


# Means
# df  0.0450223523150612
# df2 0.04026940247252747
# df3 0.037034884532198414
# df4 0.07016615698267074
# df5 0.041824836390078377


test = [df['polarity'], df2['polarity'], df3['polarity'], df4['polarity'], df5['polarity']]
t1 = pd.concat(test)
print(t1.shape)
plt.ylim(-0.03, 0.15)
t2 = t1.rolling(window=400).mean()
maa = pd.Series(data=t2.values)
maa.plot(figsize=(10, 4))
plt.ylabel("Sentiment score")
plt.xlabel("Number of Tweets")
plt.show()


