from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import os

from news_sentiment.feed_with_sentiment import feed_with_sentiment
from news_sentiment.find_opposing_articles import find_opposing_articles

app = FastAPI()

frontend_cors = os.environ['FRONTEND_ORIGIN'];

origins = [
  frontend_cors,
  "http://localhost:3000",
  "http://127.0.0.1:3000",
]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


# Default root endpoint
@app.get("/")
async def root():
  return feed_with_sentiment()


@app.get("/news")
async def news():
  return feed_with_sentiment("")


@app.get("/news/{search_term}")
async def news_with_search(search_term: str):
  return feed_with_sentiment(search_term)


@app.get("/opposing_view/{terms}")
async def opposing_view_get(terms: str, sentiment: str):
  return find_opposing_articles(terms, "", sentiment)


class OppReq(BaseModel):
  name: str
  description: str
  sentiment: str
  url: str


@app.post("/opposing_view")
async def opposing_view_post(opp_req: OppReq):
  return find_opposing_articles(opp_req.name, opp_req.description,
                                opp_req.sentiment, opp_req.url)
