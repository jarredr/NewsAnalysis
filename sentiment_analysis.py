import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analysis(data):
    
    """
    Runs sentiment analysis on news headlines.
        Parameters:
            data (list): a list of news headlines
        Returns:
            a list containing the calculated sentiment of the news headlines
    """
    # nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    result = []
    for headline in data:
        score = sia.polarity_scores(headline)["compound"]
        # These are the typical threshold values according to https://github.com/cjhutto/vaderSentiment#about-the-scoring
        if score >= 0.05:
            result.append("pos")
        elif score <= -0.05:
            result.append("neg")
        else:
            result.append("neu")
    return result



