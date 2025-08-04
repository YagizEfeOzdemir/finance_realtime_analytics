import pandas as pd
import requests
import streamlit as st

@st.cache_data
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    df = pd.read_html(url)[0]
    return df.set_index("Symbol")

def get_stock_df(symbol, api_key, time):
    url = f"https://www.alphavantage.co/query?function={time}&symbol={symbol}&apikey={api_key}"
    r = requests.get(url)
    data = r.json()

    json_key_map = {
        "TIME_SERIES_DAILY": "Time Series (Daily)",
        "TIME_SERIES_WEEKLY": "Weekly Time Series",
        "TIME_SERIES_MONTHLY": "Monthly Time Series"
    }
    json_key = json_key_map[time]
    
    if json_key not in data:
        st.error("Data could not be retrieved. Invalid symbol, time interval, or API limit exceeded.")
    return None

    df = pd.DataFrame.from_dict(data[json_key], orient="index")
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    }, inplace=True)
    return df
