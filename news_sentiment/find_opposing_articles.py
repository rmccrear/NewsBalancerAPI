from .get_news import get_news
from .clean_feed import clean_feed
from .feed_with_sentiment import anotate_with_sentiment


def find_opposing_articles(headline,
                           description="",
                           sentiment="positive",
                           url=""):
  topical_news = get_news(headline + " " + description[0:20])
  topical_news = clean_feed(topical_news)
  topical_news = [n for n in topical_news if n["url"] != url]
  topical_news = anotate_with_sentiment(topical_news)

  # sort by opposite sentiment score to the one from this article
  if (sentiment == "positive"):
    topical_news.sort(key=lambda x: 0 - x["sentiment_score"]["neg"])
  else:
    topical_news.sort(key=lambda x: 0 - x["sentiment_score"]["pos"])

  return topical_news
