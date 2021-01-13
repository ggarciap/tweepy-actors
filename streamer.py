from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import creds

# # # # CLIENT # # # #
class Tclient():
    
    def __init__(self,twitter_user=None):
        self.auth = TAuthenticator.authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_user_timeline_tweets(self, num_tweets=10):
        tweets = list()
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

class TAuthenticator():
    
    @staticmethod
    def authenticate_twitter_app():
        auth = OAuthHandler(creds.CONSUMER_KEY, creds.CONSUMER_SECRET)
        auth.set_access_token(creds.ACCESS_TOKEN, creds.ACCESS_TOKEN_SECRET)
        return auth

class TwitterStreamer():
    '''
    Class for processing plus streaming
    '''
    # def __init__(self):
    #     self.twitter_authenticator = TAuthenticator()
    def stream_tweets(self, fetched_tweets_filename, individuals):
        # Handles Twitter connection and connection to Twitter Streaming API
        listener = TListener(fetched_tweets_filename)
        auth = TAuthenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        stream.filter(track= individuals)



# Passing reference of the Class StreamListener
# Inheretance
class TListener(StreamListener):
    '''
    Basic listener class
    '''
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
        except BaseException as e:
            print(f'Error on data: {str(e)}')
        return True

    def on_error(self, data):
        if status == 420:
            'In case rate limit occurs'
            return False
        print(status)

if __name__ == "__main__":
    ind_list = 'donald trump', 'barack obama', 'AOC'
    ftf_name = 'tweets.json'

    twitter_c = Tclient('elonmusk')
    print(twitter_c.get_user_timeline_tweets(1))
    # t_streamer = TwitterStreamer()
    # t_streamer.stream_tweets(ftf_name, ind_list)

