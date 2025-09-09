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
# stock_data = response.json()
# print(stock_data)
# stock_closing_data = stock_data["Time Series (Daily)"]["2025-09-08"]["4. close"]  #"2025-09-08" its a dictioanry in the json file so make it list for dynamically get data in previous day
# print(stock_closing_data)
stock_data = response.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]   #list comprehension
# print(stock_list)
yesterday_closing_stock_data = stock_list[0]["4. close"]
print(yesterday_closing_stock_data)

