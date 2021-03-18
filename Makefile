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
	touch $@

load_data: create_tables get_data
	#head -1 tesla_stocks.csv > all_stocks.csv
	tail -n +2 -q *_stocks.csv >> all_stocks.csv
	/usr/bin/sqlite3 newsStocksWeather.sqlite -cmd ".mode csv" ".import all_stocks.csv stocks"
	#head -1 tesla_articles.csv > all_articles.csv
	tail -n +2 -q *_articles.csv >> all_articles.csv
	/usr/bin/sqlite3 newsStocksWeather.sqlite -cmd ".mode csv" ".import all_articles.csv articles"

nuke:
	rm create_tables
	rm py_env_installed
	rm -r news-stocks-weather/
	rm -r *.csv
