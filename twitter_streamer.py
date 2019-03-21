from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_keys
import re


class StdOutListener(StreamListener):
    def on_status(self, status):
        try:
            if 'RT' in status.text[0:3]:
                pass
            else:
                try:
                    text = status.extended_tweet["full_text"]
                    print(' '.join(re.sub("(@[A-Za-z0-9_]+)|(\w+:\/\/\S+)", " ", text).split()))
                except AttributeError:
                    text = status.text
                    print(' '.join(re.sub("(@[A-Za-z0-9_]+)|(\w+:\/\/\S+)", " ", text).split()))
                with open("tweets.txt", 'a') as tf:
                    tf.write(' '.join(re.sub("(@[A-Za-z0-9_]+)|(\w+:\/\/\S+)", " ", text).split()))
                    tf.write("\n")
        except UnicodeEncodeError:
            pass

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False


if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(twitter_keys.CONSUMER_KEY, twitter_keys.CONSUMER_SECRET)
    auth.set_access_token(twitter_keys.ACCESS_TOKEN, twitter_keys.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, listener, tweet_mode='extended')
    stream.filter(track=["brexit","#brexit"], languages=["en"])
