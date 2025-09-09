import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "A22188536L1NZJ2P"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
}

#--------- fetch the daily stock data ----------
response = requests.get(url=STOCK_ENDPOINT,params=stock_params)
response.raise_for_status()
stock_data = response.json()
print(stock_data)

