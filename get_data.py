import csv
import logging
import requests
from requests.auth import HTTPBasicAuth
import config
from datetime import datetime, timedelta
from utils import timethis


logger = logging.getLogger(__name__)


def get_auth_headers(api_key):
    return {
        "Content-Type": "Application/JSON",
        "Authorization": api_key
    }


def get_data(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != requests.codes.ok:
        logger.info(response.status_code)

    return response.json()


def format_data(columns_dict, data):
    formatted = dict()
    for col in columns_dict:
        if len(columns_dict[col].split("|")) == 2:
            col1, col2 = columns_dict[col].split("|")
            formatted[col] = data[col1][col2]
        else:
            formatted[col] = data[columns_dict[col]]

    return formatted


def to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, keys)
        writer.writeheader()
        writer.writerows(data)

    logger.info(f"Saved data to: {filename}")


def articles_request_params(topic, date):
    headers = get_auth_headers(config.NEWSAPI_KEY)    
 
    params = {
        "q": topic,
        "from": date,
        "to": date,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 10,
    }
    
    return get_data(config.news_get_everything, headers, params)["articles"]


def stock_price_request_params(name, date):

    params = {
        "symbol": name,
        "apikey": config.ALPHAVANTAGE_KEY,
    }

    stock_price = get_data(config.avant_daily, None, params)["Time Series (Daily)"][date]
    stock_price["symbol"] = name
    stock_price["transactions_date"] = date
    return stock_price


@timethis
def main():
    yesterday = datetime.today() - timedelta(1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    for company in config.article_keywords:
        articles = articles_request_params(company, yesterday)
        articles = [format_data(config.newsapi_columns, a) for a in articles]
        to_csv(articles, config.filenames[company])
    for company in config.stock_keywords:
        stocks = [stock_price_request_params(company, yesterday)]
        stocks = [format_data(config.avant_columns, s) for s in stocks]
        to_csv(stocks, config.filenames[company])


if __name__ == "__main__":
    main()
