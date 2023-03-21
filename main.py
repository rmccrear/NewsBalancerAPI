from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from news_sentiment.feed_with_sentiment import feed_with_sentiment

app = FastAPI()

origins = [
  "https://newssearcher.rmccrear.repl.co",
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


# Example path parameter
@app.get("/name/{name}")
async def name(name: str):
  return {"message": f"Hello {name}"}
