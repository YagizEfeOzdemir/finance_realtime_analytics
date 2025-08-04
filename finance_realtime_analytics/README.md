# 📈 Finance Realtime Analytics Dashboard

This project provides a **Streamlit-based dashboard** for visualizing real-time stock price data of **S&P 500 companies** using the **Alpha Vantage API**.

## 🚀 Features

- Select stock data for daily, weekly, or monthly intervals
- Choose from a dynamic list of S&P 500 companies
- Enter your personal Alpha Vantage API key securely
- View interactive line charts of Open, High, Low, and Close prices
- Explore raw historical stock data in a table

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/finance_realtime_analytics.git
cd finance_realtime_analytics
```

2. *(Optional)* Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

To start the Streamlit app:

```bash
streamlit run dashboard/app.py
```

Then:

- Select a time interval (Daily, Weekly, Monthly)
- Choose a company from the dropdown
- Enter your Alpha Vantage API key
- Click the **Load Data** button to fetch and view data

## 📂 Project Structure

```
finance_realtime_analytics/
├── dashboard/
│   └── app.py               # Main Streamlit UI
├── src/
│   └── fetch_data.py        # Data fetching and preprocessing
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 🔑 API Key Info

- This app uses [Alpha Vantage API](https://www.alphavantage.co/).
- You must sign up and get your free API key.
- Free tier allows up to **5 requests/minute** and **500 requests/day**.

## 📌 Notes

- The list of S&P 500 companies is dynamically scraped from [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
- Make sure to respect Alpha Vantage's rate limits.


