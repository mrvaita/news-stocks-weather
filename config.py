import logging
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# API-KEYS (Need to take care of this)
NEWSAPI_KEY = "6fde7d1a1a364f9b92cca6783cb4ed5b"
ALPHAVANTAGE_KEY = "7OODLY05NRHN65KW"
WEATHERBIT_KEY = "a91b1a6561eb4550a4070e2f21e07579"

# Keywords for News and stocks
article_keywords = ["bitcoin", "mars", "tesla"]
stock_keywords = ["BTCUSD", "TSLA"]
city_ids = ["5128581", "2643741", "1796236", "1819729" ,"1850147", "4641630"]

# NewsAPI base string
news_get_everything = "https://newsapi.org/v2/everything?"
avant_daily = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"
weatherbit_hist_daily = "https://api.weatherbit.io/v2.0/history/daily"

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

weatherbit_columns = {
    "city_name": "city_name",
    "city_id": "city_id",
    "acquired_on": "datetime", 
    "wind_speed_avg": "wind_spd",
    "temperature_avg": "temp",
    "min_temperature": "min_temp",
    "max_temperature": "max_temp",
    "precipitation": "precip",
    "snow": "snow",
}

filenames = {
    "bitcoin": "bitcoin_articles.csv",
    "mars": "mars_articles.csv",
    "tesla": "tesla_articles.csv",
    "BTCUSD": "bitcoin_stocks.csv",
    "TSLA": "tesla_stocks.csv",
    "5128581": "newyork_weather.csv",
    "2643741": "london_weather.csv",
    "1796236": "shangay_weather.csv",
    "1819729": "hongkong_weather.csv",
    "1850147": "tokyo_weather.csv",
    "4641630": "milan_weather.csv",
}
city_ids = ["5128581", "2643741", "1796236", "1819729" ,"1850147", "4641630"]
