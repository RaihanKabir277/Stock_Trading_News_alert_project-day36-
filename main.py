import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "A22188536L1NZJ2P"
NEWS_API_KEY = "a791e4b3f1194739918a0f35730cd37d"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
}

#--------- fetch the daily stock data and save the previos day closing data----------
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
# print(yesterday_closing_stock_data)

# --------------- Get the day before yesterday's closing stock price ------------
day_before_yesterday_closing_data = stock_list[1]["4. close"]
# print(day_before_yesterday_closing_data)

# ------- comapre two days data ---------
positive_diff = abs(float(yesterday_closing_stock_data) - float(day_before_yesterday_closing_data))
# print(positive_diff)

# ------- the percenatge difference of two days and call news api ------------
diff_pecentage = (positive_diff / float(yesterday_closing_stock_data)) * 100
# print(diff_pecentage)

if diff_pecentage > 0:
    news_params = {
        "apikey" : NEWS_API_KEY,
        "q" : COMPANY_NAME,
    }
    news_response = requests.get(url=NEWS_ENDPOINT,params=news_params)
    news_response.raise_for_status()
    news_articles = news_response.json()["articles"]
    # -----slicing for get at first 3 articles -------
    three_articles =news_articles[:3]
    # print(three_articles)
    formatted_news_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_news_list)




