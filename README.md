# 📈 Tesla Stock & News Alert System

A Python project that tracks **Tesla's (TSLA)** stock price using the [Alpha Vantage API](https://www.alphavantage.co) and, when there is a significant change, fetches the latest related news articles from the [NewsAPI](https://newsapi.org). The system is also designed to send alerts via **Twilio SMS** for real-time notifications.

---

## 🚀 Features

- Fetches **daily stock data** for Tesla (TSLA) using Alpha Vantage.
- Automatically compares **yesterday’s** and **day before yesterday’s** closing prices.
- Calculates **percentage change** in stock price.
- If change exceeds the threshold, retrieves the **latest 3 Tesla-related news headlines** from NewsAPI.
- Formats news output neatly with headline and brief.
- Ready to integrate with **Twilio** for SMS alerts.

---

## 🛠️ Tech Stack

- **Python 3**
- **Requests** – for making API calls
- **Alpha Vantage API** – stock data
- **NewsAPI** – news articles
- **Twilio (optional)** – SMS notifications

---

## 📂 Project Structure

- ├── main.py # Main script
- ├── requirements.txt # Required Python libraries
- └── README.md # Project documentation


---

## ⚙️ Setup Instructions

**Clone the Repository**
   ```bash
   git clone https://github.com/RaihanKabir277/Stock_Trading_News_alert_project-day36-.git

---
- export STOCK_API_KEY="your_alpha_vantage_api_key"
- export NEWS_API_KEY="your_newsapi_key"
- export TWILIO_SID="your_twilio_sid"
- export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
---
# Run the Script

python main.py

   
