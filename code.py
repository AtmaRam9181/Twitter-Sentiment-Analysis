import tweepy
from textblob import TextBlob

# Twitter API credentials (you need to replace these with your own credentials)
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def get_tweets(query, count=100):
    """
    Function to fetch tweets based on a query.
    """
    tweets = []
    try:
        fetched_tweets = api.search(q=query, count=count)
        for tweet in fetched_tweets:
            parsed_tweet = {}
            parsed_tweet['text'] = tweet.text
            parsed_tweet['sentiment'] = analyze_sentiment(tweet.text)
            tweets.append(parsed_tweet)
    except tweepy.TweepError as e:
        print("Error : " + str(e))
    
    return tweets

def analyze_sentiment(text):
    """
    Function to analyze sentiment of a given text.
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def main():
    # Enter the Premier League team name you want to analyze
    team_name = "Manchester United"
    tweets = get_tweets(query=team_name, count=100)
    
    positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutral_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    
    # Print sentiment analysis results
    print("Sentiment analysis of tweets about", team_name)
    print("Positive tweets: ", len(positive_tweets))
    print("Negative tweets: ", len(negative_tweets))
    print("Neutral tweets: ", len(neutral_tweets))

if __name__ == "__main__":
    main()
