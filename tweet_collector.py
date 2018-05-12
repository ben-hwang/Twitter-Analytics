from twython import TwythonStreamer
import sys
import json
 
# array to hold all tweets
tweets = []

# Keyword to search
keyword_user = input("What keyword would you like to search? ")

# Number of tweets to collect
no_of_tweets = eval(input("How many tweets would you like to collect? "))


# inheriting from TwythonStreamer 
# Github Code: https://github.com/ryanmcgrath/twython/blob/master/twython/streaming/api.py
class MyStreamer(TwythonStreamer):

    # overriding on_success function
    def on_success(self, data):

        # check if the received tweet dictionary is in English
        if 'lang' in data and data['lang'] == 'en':
            tweets.append(data)
            print('received tweet #', len(tweets), data['text'][:100])
 
        # if we have enough tweets(user-inputted), store into JSON file and disconnect API 
        if len(tweets) >= no_of_tweets:
            self.store_json()
            self.disconnect()

    # overriding on_error function
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()
 
    # our new method to store tweets into JSON file
    def store_json(self):
        with open('{}_{}.json'.format(keyword_user, len(tweets)), 'w') as f:
            json.dump(tweets, f, indent=4)
 
# check if we are top-level module
if __name__ == '__main__':
 
    #open my twitter credentials and load it into a dictionary
    with open('ben_twitter_credentials.json', 'r') as creds:
        credentials = json.load(creds)
 
    # get my own consumer_key and other info
    CONSUMER_KEY = credentials['CONSUMER_KEY']
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']
    ACCESS_TOKEN = credentials['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']
 
    # Twitter Streaming API needs my Twitter account credentials, stored in a separate JSON file
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    # https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter
    stream.statuses.filter(track=keyword_user)