import json


def get_news(search_term=""):
  f = open('news_sentiment/mock_data/news.json')

  news_data = json.load(f)
  return news_data
