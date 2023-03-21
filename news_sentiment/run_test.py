from .get_data import get_news
from .clean_feed import clean_feed
from .sentiment import sentiment_scores

news_data = get_news()
articles = clean_feed(news_data)

# leads = [article["lead"] for article in articles]

#print(leads)

#scores = sentiment_scores(leads)

#print(scores)


def anotate_with_sentiment(articles):
  leads = [article["lead"] for article in articles]
  scores = sentiment_scores(leads)
  for article, score in zip(articles, scores):
    article["sentiment_score"] = score
  return articles


print(anotate_with_sentiment(articles))