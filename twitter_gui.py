import twitter_keys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from textblob import TextBlob
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import re
import sys
import datetime
import tkinter as tk
from tkinter import ttk


class TwitterClient:
    def __init__(self):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=text_entry.get()+" -filter:retweets", lang="en", tweet_mode="extended", count=3000).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_tweets1(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=text_entry.get()+" -filter:retweets", lang="en", tweet_mode="extended", until=Date, count=3000).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_tweets3(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=text_entry.get()+" -filter:retweets", lang="en", tweet_mode="extended", until=Date - datetime.timedelta(days=2), count=3000).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_tweets21(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=double_entry.get()+" -filter:retweets", lang="en", tweet_mode="extended", count=1500).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_tweets22(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=double_entry1.get()+" -filter:retweets", lang="en", tweet_mode="extended", count=1500).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_tweets211(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=double_entry.get()+" -filter:retweets", lang="en", tweet_mode="extended", until=Date, count=1500).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_tweets213(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=double_entry1.get()+" -filter:retweets", lang="en", tweet_mode="extended", until=Date, count=1500).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_tweets221(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=double_entry.get()+" -filter:retweets", lang="en", tweet_mode="extended", until=Date - datetime.timedelta(days=2), count=1500).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_tweets223(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=double_entry1.get()+" -filter:retweets", lang="en", tweet_mode="extended", until=Date - datetime.timedelta(days=2), count=1500).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_user_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=user_entry.get(), tweet_mode="extended", count=1500).items(num_tweets):
            tweets.append(tweet)
        return tweets


class TwitterAuthenticator:
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_keys.CONSUMER_KEY, twitter_keys.CONSUMER_SECRET)
        auth.set_access_token(twitter_keys.ACCESS_TOKEN, twitter_keys.ACCESS_TOKEN_SECRET)
        return auth


class TweetAnalyzer:
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9_]+)|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_polarity(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        pol = round(analysis.sentiment.polarity, 3)
        return pol

    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame()
        df['Tweets'] = np.array([tweet.full_text for tweet in tweets])
        df['Polarity'] = np.array([analyzer.analyze_polarity(tweet) for tweet in df['Tweets']])
        return df


class StdOutListener(StreamListener):
    def on_status(self, status):
        try:
            if 'RT' in status.text[0:3]:
                pass
            else:
                try:
                    text = status.extended_tweet["full_text"]
                except AttributeError:
                    text = status.text
                with open("text.txt", 'a') as tf:
                    tf.write(' '.join(re.sub("(@[A-Za-z0-9_]+)|(\w+:\/\/\S+)", " ", text).split()))
                    tf.write("\n")
        except UnicodeEncodeError:
            pass

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False


class Gui:
    def analysis(self):
        search = text_entry.get()
        print("Gathering tweets...")
        tweets1 = client.get_tweets(3000)
        df1 = analyzer.tweets_to_data_frame(tweets1)
        df1['MA'] = df1['Polarity'].rolling(window=30).mean()
        polarity = pd.Series(data=df1['Polarity'].values)
        polarity.plot(figsize=(16, 4))
        ma = pd.Series(data=df1['MA'].values)
        ma.plot(figsize=(16, 4))
        plt.title("Sentiment scores for keyword: " + search)
        plt.ylabel("Sentiment score")
        plt.xlabel("Number of Tweets")
        plt.show()

    def analysis1(self):
        search = text_entry.get()
        print("Gathering tweets...")
        tweets1 = client.get_tweets1(3000)
        df1 = analyzer.tweets_to_data_frame(tweets1)
        df1['MA'] = df1['Polarity'].rolling(window=30).mean()
        polarity = pd.Series(data=df1['Polarity'].values)
        polarity.plot(figsize=(16, 4))
        ma = pd.Series(data=df1['MA'].values)
        ma.plot(figsize=(16, 4))
        plt.title("Sentiment scores for keyword: " + search)
        plt.ylabel("Sentiment score")
        plt.xlabel("Number of Tweets")
        plt.show()

    def analysis3(self):
        search = text_entry.get()
        print("Gathering tweets...")
        tweets1 = client.get_tweets3(3000)
        df1 = analyzer.tweets_to_data_frame(tweets1)
        df1['MA'] = df1['Polarity'].rolling(window=30).mean()
        polarity = pd.Series(data=df1['Polarity'].values)
        polarity.plot(figsize=(16, 4))
        ma = pd.Series(data=df1['MA'].values)
        ma.plot(figsize=(16, 4))
        plt.title("Sentiment scores for keyword: " + search)
        plt.ylabel("Sentiment score")
        plt.xlabel("Number of Tweets")
        plt.show()

    def analysis2(self):
        search1 = double_entry.get()
        search2 = double_entry1.get()
        print("Gathering tweets...")
        tweets1 = client.get_tweets21(1500)
        df1 = analyzer.tweets_to_data_frame(tweets1)
        df1['MA'] = df1['Polarity'].rolling(window=15).mean()
        ma1 = pd.Series(data=df1['MA'].values)
        ma1.plot(figsize=(16, 4), label=search1, legend=True)
        tweets2 = client.get_tweets22(1500)
        df2 = analyzer.tweets_to_data_frame(tweets2)
        df2['MA'] = df2['Polarity'].rolling(window=15).mean()
        ma2 = pd.Series(data=df2['MA'].values)
        ma2.plot(figsize=(16, 4), label=search2, legend=True)
        plt.title("Sentiment scores for keywords: " + search1 + " & " + search2)
        plt.ylabel("Sentiment score")
        plt.xlabel("Number of Tweets")
        plt.show()

    def analysis21(self):
        search1 = double_entry.get()
        search2 = double_entry1.get()
        print("Gathering tweets...")
        tweets1 = client.get_tweets211(1500)
        df1 = analyzer.tweets_to_data_frame(tweets1)
        df1['MA'] = df1['Polarity'].rolling(window=15).mean()
        ma1 = pd.Series(data=df1['MA'].values)
        ma1.plot(figsize=(16, 4), label=search1, legend=True)
        tweets2 = client.get_tweets213(1500)
        df2 = analyzer.tweets_to_data_frame(tweets2)
        df2['MA'] = df2['Polarity'].rolling(window=15).mean()
        ma2 = pd.Series(data=df2['MA'].values)
        ma2.plot(figsize=(16, 4), label=search2, legend=True)
        plt.title("Sentiment scores for keywords: " + search1 + " & " + search2)
        plt.ylabel("Sentiment score")
        plt.xlabel("Number of Tweets")
        plt.show()

    def analysis23(self):
        search1 = double_entry.get()
        search2 = double_entry1.get()
        print("Gathering tweets...")
        tweets1 = client.get_tweets221(1500)
        df1 = analyzer.tweets_to_data_frame(tweets1)
        df1['MA'] = df1['Polarity'].rolling(window=15).mean()
        ma1 = pd.Series(data=df1['MA'].values)
        ma1.plot(figsize=(16, 4), label=search1, legend=True)
        tweets2 = client.get_tweets223(1500)
        df2 = analyzer.tweets_to_data_frame(tweets2)
        df2['MA'] = df2['Polarity'].rolling(window=15).mean()
        ma2 = pd.Series(data=df2['MA'].values)
        ma2.plot(figsize=(16, 4), label=search2, legend=True)
        plt.title("Sentiment scores for keywords: " + search1 + " & " + search2)
        plt.ylabel("Sentiment score")
        plt.xlabel("Number of Tweets")
        plt.show()

    def user_analysis(self):
        user_search = user_entry.get()
        print("Gathering tweets...")
        user_tweets = client.get_user_tweets(3000)
        df1 = analyzer.tweets_to_data_frame(user_tweets)
        df1['MA'] = df1['Polarity'].rolling(window=30).mean()
        polarity = pd.Series(data=df1['Polarity'].values)
        polarity.plot(figsize=(16, 4))
        ma = pd.Series(data=df1['MA'].values)
        ma.plot(figsize=(16, 4))
        plt.title("Sentiment scores for user: @" + user_search)
        plt.ylabel("Sentiment score")
        plt.xlabel("Number of Tweets")
        plt.show()

    def image(self):
        img = mpimg.imread('Figure_1.png')
        f, a = plt.subplots(figsize=(16, 4))
        plt.tight_layout()
        plt.axis('off')
        a.imshow(img)
        plt.show()

    def stream(self):
        xd = stream_entry.get()
        root = tk.Tk()
        root.title("Live graph")
        fig = plt.figure()

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(row=1, column=0)

        with open("text.txt", "w") as truncate_file:
            truncate_file.truncate()

        def animate(i):
            raw_data = open("text.txt", "r+").read()
            raw_array = raw_data.split('\n')
            analysis = TweetAnalyzer()
            score_data = open("score.txt", 'w+')
            x = 0
            for Line in raw_array:
                x += 1
                pol = analysis.analyze_polarity(Line)
                #print(Line)
                #print(pol)
                score_data.write(str(x) + "," + str(pol))
                score_data.write('\n')
            score_data.close()
            pull_data = open("score.txt", "r").read()
            data_array = pull_data.split('\n')
            xar = []
            yar = []
            for Line in data_array:
                if len(Line) > 1:
                    x, y = Line.split(',')
                    xar.append(float(x))
                    yar.append(float(y))
            ax1.clear()
            ax1.plot(xar, yar)
            df0 = pd.DataFrame()
            df0['Polarity'] = np.array(yar)
            df0['MA'] = df0['Polarity'].rolling(window=20).mean()
            ma = pd.Series(data=df0['MA'].values)
            ax1.plot(ma)
            plt.title("Sentiment scores for keyword: " + xd)
            plt.ylabel("Sentiment score")
            plt.xlabel("Number of Tweets")
                
        ax1 = fig.add_subplot(111)

        listener = StdOutListener()
        auth = OAuthHandler(twitter_keys.CONSUMER_KEY, twitter_keys.CONSUMER_SECRET)
        auth.set_access_token(twitter_keys.ACCESS_TOKEN, twitter_keys.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener, tweet_mode='extended')
        stream.filter(track=[xd], languages=["en"], async=True)

        ani = animation.FuncAnimation(fig, animate, interval=500, blit=False)

        ttk.Button(root, text="Stop", command=stream.disconnect).grid(row=2, column=0)

        def leave():
            root.destroy()
            stream.disconnect()

            def handle_close():
                print('Closed Figure!')

            canvas.mpl_connect('close_event', handle_close)
            plt.clf()
            plt.cla()
            plt.close(fig)
            plt.close('all')

        ttk.Button(root, text="Exit", command=leave).grid(row=3, column=0)
        tk.mainloop()


if __name__ == '__main__':

    client = TwitterClient()
    authenticator = TwitterAuthenticator()
    analyzer = TweetAnalyzer()
    api = client.get_twitter_client_api()
    gui = Gui()
    pd.set_option('max_colwidth', 300)
    Date = datetime.datetime.now()
    Date = Date.date()
    Time = datetime.datetime.now()
    window = tk.Tk()
    topFrame = ttk.Frame(window, width=800, height=600)
    topFrame.grid(row=0)
    window.title("Sentiment analysis GUI")
    window.resizable(0, 0)
    logo = tk.PhotoImage(file="logo.png")
    background = ttk.Label(window, image=logo)
    background.grid(row=0, sticky="nsew")
    background.columnconfigure(0, weight=1)
    ttk.Label(background, text="Enter the keyword you want to search for:").grid(row=1)
    text_entry = ttk.Entry(background, width=20)
    text_entry.grid(row=2)
    ttk.Button(background, text="Latest", command=gui.analysis).grid(row=3)
    ttk.Button(background, text="Yesterday", command=gui.analysis1).grid(row=4)
    ttk.Button(background, text="3-day", command=gui.analysis3).grid(row=5)
    ttk.Label(background, text="Enter the two keywords you want to compare and search for:").grid(row=6)
    background.rowconfigure(6, weight=1)
    double_entry = ttk.Entry(background, width=20)
    double_entry.grid(row=7)
    double_entry1 = ttk.Entry(background, width=20)
    double_entry1.grid(row=8)
    ttk.Button(background, text="Latest", command=gui.analysis2).grid(row=9)
    ttk.Button(background, text="Yesterday", command=gui.analysis21).grid(row=10)
    ttk.Button(background, text="3-day", command=gui.analysis23).grid(row=11)
    ttk.Label(background, text="Enter the Twitter username you want to search:").grid(row=12)
    background.rowconfigure(12, weight=1)
    user_entry = ttk.Entry(background, width=20)
    user_entry.grid(row=13)
    ttk.Button(background, text="Submit", command=gui.user_analysis).grid(row=14)
    ttk.Label(background, text="Refer to the case study below:").grid(row=15)
    background.rowconfigure(15, weight=1)
    ttk.Button(background, text="Brexit", command=gui.image).grid(row=16)
    ttk.Label(background, text="Live graph:").grid(row=17)
    background.rowconfigure(17, weight=1)
    stream_entry = ttk.Entry(background, width=20)
    stream_entry.grid(row=18)
    ttk.Button(background, text="Go", command=gui.stream).grid(row=19)
    ttk.Label(background, text="To quit click below:").grid(row=20)
    ttk.Button(background, text="Exit", command=sys.exit).grid(row=21)
    window.mainloop()

