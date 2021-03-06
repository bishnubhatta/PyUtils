import tweepy
import json
import ConfigParser

# Authentication details. To  obtain these visit dev.twitter.com
config = ConfigParser.ConfigParser()
config.read('C:/Pysocial/twitter.conf')
consumer_key = config.get('twitter_details', 'consumer_key')
consumer_secret = config.get('twitter_details', 'consumer_secret')
access_token = config.get('twitter_details', 'access_token')
access_token_secret = config.get('twitter_details', 'access_token_secret')

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets for Modi:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['Mauka'])