from .clean_feed import clean_article


def annotate_with_opposing_viewpoint(articles):
  max_neg_article = articles[0]
  max_pos_article = articles[0]
  for article in articles:
    print(article)
    if (article["sentiment_score"]["neg"] >
        max_neg_article["sentiment_score"]["neg"]):
      max_neg_article = article  # to avoid cycles in json
    if (article["sentiment_score"]["pos"] >
        max_pos_article["sentiment_score"]["pos"]):
      max_pos_article = article  # to avoid cycles in json

  for article in articles:
    print(article["name"])
    if (article["sentiment_score"]["neg"] > article["sentiment_score"]["pos"]):
      article["sentiment"] = "negative"
      article["opposing_views"] = [clean_article(max_pos_article)]
    else:
      article["sentiment"] = "positive"
      article["opposing_views"] = [clean_article(max_neg_article)]
  return articles
