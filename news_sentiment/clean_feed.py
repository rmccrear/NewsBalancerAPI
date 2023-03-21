import html


def clean_article(article):
  return {
    "lead": article["name"] + " " + article["description"],
    "name": article["name"],
    "description": article["description"],
    "image": article.get("image", ""),
    "url": article["url"],
    "sentiment_score": article.get("sentiment_score", {}),
    "sentiment": article.get("sentiment", "")
  }


def unescape_lead(article):
  article["lead"] = html.unescape(article["lead"])


# input search results from /news/search
def clean_feed(news_data):
  feed = [clean_article(article) for article in news_data["value"]]
  for article in feed:
    unescape_lead(article)
  return feed
