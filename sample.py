import tweepy
from textblob import TextBlob

# Sample tweet data for Premier League teams
sample_tweets = {
    "Manchester United": [
        "Manchester United played incredibly well today! #MUFC",
        "Disappointed with Manchester United's performance. #MUFC",
        "Can't wait for the next Manchester United game! #GGMU"
    ],
    "Liverpool": [
        "Liverpool is unstoppable this season. #LFC",
        "Another win for Liverpool! #YNWA",
        "Liverpool needs to improve their defense. #LFC"
    ],
    "Manchester City": [
        "Manchester City with another dominant performance. #MCFC",
        "Disappointed with Manchester City's loss. #MCFC",
        "Manchester City is the best team in the league! #CTID"
    ],
    "Arsenal": [
        "Arsenal's defense needs serious improvement. #AFC",
        "Great game by Arsenal today! #COYG",
        "I'm losing faith in Arsenal's ability to win. #AFC"
    ],
    "Chelsea": [
        "Chelsea played exceptionally well today. #CFC",
        "Chelsea's new signing is a game-changer! #CFC",
        "Disappointed with Chelsea's draw. #KTBFFH"
    ],
    "Tottenham Hotspur": [
        "Tottenham Hotspur with a stunning comeback! #THFC",
        "Tottenham Hotspur needs to strengthen their midfield. #COYS",
        "I'm proud to be a Tottenham Hotspur fan! #THFC"
    ]
}

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
    team_sentiment = {}
    
    # Analyzing sentiment for each Premier League team
    for team, tweets in sample_tweets.items():
        positive_count = 0
        negative_count = 0
        neutral_count = 0
        
        for tweet in tweets:
            sentiment = analyze_sentiment(tweet)
            if sentiment == 'positive':
                positive_count += 1
            elif sentiment == 'negative':
                negative_count += 1
            else:
                neutral_count += 1
        
        # Calculating sentiment score
        sentiment_score = positive_count - negative_count
        
        team_sentiment[team] = sentiment_score
    
    # Sorting teams based on sentiment score
    sorted_teams = sorted(team_sentiment.items(), key=lambda x: x[1], reverse=True)
    
    # Printing results
    print("Premier League teams sentiment analysis based on sample tweets:")
    for team, sentiment_score in sorted_teams:
        print(f"{team}: {sentiment_score}")
    

if __name__ == "__main__":
    main()
	