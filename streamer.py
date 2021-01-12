from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import creds

class TwitterStreamer():
    '''
    Class for processing plus streaming
    '''
    def stream_tweets(self, fetched_tweets_filename, individuals):
        # Handles Twitter connection and connection to Twitter Streaming API
        listener = stdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(creds.CONSUMER_KEY, creds.CONSUMER_SECRET)
        auth.set_access_token(creds.ACCESS_TOKEN, creds.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)

        stream.filter(track= individuals)




class stdOutListener(StreamListener):
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
        print(status)

if __name__ == "__main__":
    ind_list = 'donald trump', 'barack obama', 'AOC'
    ftf_name = 'tweets.json'

    t_streamer = TwitterStreamer()
    t_streamer.stream_tweets(ftf_name, ind_list)

