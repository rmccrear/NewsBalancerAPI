import nltk

nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


def sentiment_scores(docs):
  return [sia.polarity_scores(doc) for doc in docs]
