import json
from textblob import TextBlob 
import matplotlib.pyplot as plt
import math

keyword = input("What was the keyword? ")
no_of_tweets = eval(input("How many tweets did you collect? "))

tweet_data = open(keyword + "_" + str(no_of_tweets) + ".json")

tweet_data_parsed = json.load(tweet_data)

def sentiment_analysis():
    all_tweets = []

    for element in tweet_data_parsed:
        all_tweets.append(element["text"])

    sub_list = []
    pol_list = []

    for tweet in all_tweets:
    	tb = TextBlob(tweet)
    	sub_list.append(tb.sentiment.subjectivity)
    	pol_list.append(tb.sentiment.polarity)
        
    plt.hist(sub_list, bins=10) 	
    plt.xlabel('subjectivity score')
    plt.ylabel('tweet count')
    plt.grid(True)
    plt.savefig(keyword + '_' + 'subjectivity.pdf')
    plt.show()

    plt.hist(pol_list, bins=10) 
    plt.xlabel('polarity score')
    plt.ylabel('tweet count')
    plt.grid(True)
    plt.savefig(keyword + '_' 'polarity.pdf')
    plt.show()

sentiment_analysis() 
