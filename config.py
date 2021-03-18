import logging
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# API-KEYS (Need to take care of this)
NEWSAPI_KEY = "6fde7d1a1a364f9b92cca6783cb4ed5b"
ALPHAVANTAGE_KEY = "7OODLY05NRHN65KW"

# Keywords for News and stocks
article_keywords = ["bitcoin", "mars", "tesla"]
stock_keywords = ["BTCUSD", "TSLA"]

# NewsAPI base string
news_get_everything = "https://newsapi.org/v2/everything?"
avant_daily = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"

# Column conversions
avant_columns = {
    "symbol": "symbol",
    "open": "1. open",
    "high": "2. high",
    "low": "3. low",
    "close": "4. close",
    "adjusted_close": "5. adjusted close",
    "volume": "6. volume",
    "transactions_date": "transactions_date",
}

newsapi_columns = {
    "source_id": "source|id",
    "source_name": "source|name",
    "author": "author",
    "title": "title",
    "description": "description",
    "url": "url",
    "url_to_image": "urlToImage",
    "published_at": "publishedAt",
    "content": "content",
}

filenames = {
    "bitcoin": "bitcoin_articles.csv",
    "mars": "mars_articles.csv",
    "tesla": "tesla_articles.csv",
    "BTCUSD": "bitcoin_stocks.csv",
    "TSLA": "tesla_stocks.csv",
}
