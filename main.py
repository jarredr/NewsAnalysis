from collections import Counter
from news_headlines import abc_headlines, news_dotcomau_headlines, smh_headlines, nine_headlines, australian_headlines, guardian_headlines, sbs_headlines, skynews_headlines
from sentiment_analysis import sentiment_analysis


def count_sentiment(sentiment):
    """
    Returns the frequency of each sentiment.
        Parameters:
            sentiment (list): the sentiment values
        Returns:
            a dictionary containing the frequency of each sentiment value

    """
    counts = {'pos': 0, 'neu': 0, 'neg': 0}
    for item in sentiment:
        counts[item] += 1
    print(counts)

if __name__ == "__main__":
    count_sentiment(sentiment_analysis(abc_headlines()))
    count_sentiment(sentiment_analysis(news_dotcomau_headlines()))
    count_sentiment(sentiment_analysis(smh_headlines()))
    count_sentiment(sentiment_analysis(nine_headlines()))
    count_sentiment(sentiment_analysis(australian_headlines()))
    count_sentiment(sentiment_analysis(guardian_headlines()))
    count_sentiment(sentiment_analysis(sbs_headlines()))
    count_sentiment(sentiment_analysis(skynews_headlines()))

