import json
from collections import Counter
import nltk

keyword = input("What was the keyword? ")
no_of_tweets = eval(input("How many tweets did you collect? "))

tweet_data = open(keyword + "_" + str(no_of_tweets) + ".json")

tweet_data_parsed = json.load(tweet_data)

# finds the 10 most common words, not including stop words
def most_common_words():
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append('rt')
    stopwords.append('-')
    stopwords.append('.')
    stopwords.append('@')
   
    all_tweets = []

    for element in tweet_data_parsed:
        all_tweets.append(element["text"])

    all_words = []
    new_all_words = []

    for tweet in all_tweets:
        all_words.append(tweet.split())

    for x in all_words:
        for word in x:
            if word.lower() not in stopwords:
                new_all_words.append(word)
              
    c = Counter(new_all_words)
    return c.most_common(10)

# finds the 10 most popular hashtags
def most_popular_hashtags():
    all_hashtags = []

    for element in tweet_data_parsed:
        for hashtag in element["entities"]["hashtags"]:
            all_hashtags.append(hashtag["text"])

    c = Counter(all_hashtags)
    return c.most_common(10)

# finds the most influential parent tweet (most retweets and replies)
def most_influential_parent_tweet():
    all_tweets = {}
    influential_tweet = ""
    acc = 0

    for element in tweet_data_parsed:
        if 'retweeted_status' in element:
            all_tweets[element["retweeted_status"]["text"]] = element["retweeted_status"]["retweet_count"] + element["retweeted_status"]["reply_count"]

    for tweet in all_tweets.keys():
        if all_tweets[tweet] > acc:
            acc = all_tweets[tweet]
            influential_tweet = tweet

    return influential_tweet

print("Ten most common words: " + str(most_common_words()))
print("Ten most popular hashtags: " + str(most_popular_hashtags()))
print("Most influential tweet: " + str(most_influential_parent_tweet()))

       






