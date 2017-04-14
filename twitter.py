import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
 
consumer_key = 'DcN6YL97BORO7HEuQwOyhx9ud'
consumer_secret = '5EoQe1Cd4QtVYGeo0QabRpPu4ZUCqk7vFVSnDO8GSZAbpaW096'
access_token = '382571849-zVA2snmHrt1DjO9oatwNU1pJUoHTdUiKFXDbswgg'
access_secret = 'thW3Bjc2MwhJsqzJGejd22h3htSt0HbRCf3ig9V0WZn07'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


 
class MyListener(StreamListener):
	
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            #print(&quot;Error on_data: %s&quot; % str(e))
            pass
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(locations=[72.894051,18.720530,75.833797,22.705543])
twitter_stream.filter(locations=[77.397094, 12.733804, 78.041880, 13.301466])