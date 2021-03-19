SHELL:=/bin/bash

py_env_installed:
	python3 -m venv news-stocks-weather
	./news-stocks-weather/bin/pip install -r requirements.txt
	touch $@

get_data: py_env_installed
	./news-stocks-weather/bin/python get_data.py

create_tables:
	/usr/bin/sqlite3 newsStocksWeather.sqlite < create_articles.sql
	/usr/bin/sqlite3 newsStocksWeather.sqlite < create_stocks.sql
	/usr/bin/sqlite3 newsStocksWeather.sqlite < create_weather.sql
	touch $@

load_data: create_tables get_data
	tail -n +2 -q *_stocks.csv >> all_stocks.csv
	/usr/bin/sqlite3 newsStocksWeather.sqlite -cmd ".mode csv" ".import all_stocks.csv stocks"
	tail -n +2 -q *_articles.csv >> all_articles.csv
	/usr/bin/sqlite3 newsStocksWeather.sqlite -cmd ".mode csv" ".import all_articles.csv articles"
	tail -n +2 -q *_weather.csv >> all_weather.csv
	/usr/bin/sqlite3 newsStocksWeather.sqlite -cmd ".mode csv" ".import all_weather.csv weather"

nuke:
	rm create_tables
	rm py_env_installed
	rm -r news-stocks-weather/
	rm -r *.csv
