import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import twitter_gui as tg
from collections import Counter
from wordcloud import WordCloud

tg = tg.TweetAnalyzer()

df = pd.read_fwf('friday23-11.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
df['polarity'] = np.array([tg.analyse_polarity(tweet) for tweet in df['Tweets']])
df2 = pd.read_fwf('saturday24-11.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
df2['polarity'] = np.array([tg.analyse_polarity(tweet) for tweet in df2['Tweets']])
df3 = pd.read_fwf('sunday25-11.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
df3['polarity'] = np.array([tg.analyse_polarity(tweet) for tweet in df3['Tweets']])
df4 = pd.read_fwf('monday26-11.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
df4['polarity'] = np.array([tg.analyse_polarity(tweet) for tweet in df4['Tweets']])
df5 = pd.read_fwf('tuesday27-11.txt', delimiter="\n", dtype=str, header=None, names=['Tweets'])
df5['polarity'] = np.array([tg.analyse_polarity(tweet) for tweet in df5['Tweets']])
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


def analysis():

    pol = [df['polarity'], df2['polarity'], df3['polarity'], df4['polarity'], df5['polarity']]
    t1 = pd.concat(pol)
    plt.ylim(-0.03, 0.15)
    t2 = t1.rolling(window=400).mean()
    maa = pd.Series(data=t2.values)
    plt.subplot(3, 1, 1)
    maa.plot(figsize=(10, 4))
    plt.ylabel("Sentiment score")
    plt.xlabel("Number of Tweets")

    concat = pd.concat([df['Tweets'], df2['Tweets'], df3['Tweets'], df4['Tweets'], df5['Tweets']])
    t11 = concat.to_string()
    yy = tg.clean_tweet(t11)
    yyy = yy.lower().split()
    d = dict(Counter(yyy).most_common(15))
    kk = []
    vv = []
    for k, v in d.items():
        kk.append(k)
        vv.append(v)
    plt.subplot(3, 1, 2)
    plt.pie(vv, labels=kk)

    plt.subplot(3, 1, 3)
    word_cloud = WordCloud(collocations=False).generate(yy)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()


analysis()
