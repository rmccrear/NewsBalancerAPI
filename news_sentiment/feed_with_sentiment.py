# from .get_data import get_news  # fake data
from .get_news import get_news  # fetch from API

from .clean_feed import clean_feed
from .sentiment import sentiment_scores
from .opposing_sentiments import annotate_with_opposing_viewpoint

news_data = get_news()
articles = clean_feed(news_data)


def anotate_with_sentiment(articles):
  leads = [article["lead"] for article in articles]
  scores = sentiment_scores(leads)
  for article, score in zip(articles, scores):
    article["sentiment_score"] = score
  return articles


from functools import lru_cache


@lru_cache(maxsize=1000)
def feed_with_sentiment(search_term=""):
  # def feed_with_sentiment():
  news_data = get_news(search_term)
  articles = clean_feed(news_data)
  articles = anotate_with_sentiment(articles)
  articles = annotate_with_opposing_viewpoint(articles)
  return articles
