import streamlit as st
import pandas as pd
import sys
import os
from src.fetch_data import get_stock_df, load_data

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


zaman_araligi = ["Daily", "Weekly", "Monthly"]
components = load_data()

# Label fonksiyonu
def label(symbol):
    name = components.loc[symbol]["Security"]
    return f"{symbol} ({name})"

# UI başlıyor
st.title("📈 Stock Data")

time_period = st.selectbox("Select a time interval:", options=zaman_araligi)
sembol = st.selectbox("Select a company:", options=components.index.sort_values(), format_func=label)
api_key = st.text_input("Alpha Vantage API Key:", type="password")


time_series_key_map = {
    "Daily": "TIME_SERIES_DAILY",
    "Weekly": "TIME_SERIES_WEEKLY",
    "Monthly": "TIME_SERIES_MONTHLY"
}
time = time_series_key_map[time_period]
symbol = sembol


if st.button("Load Data"):
    if time and symbol and api_key:
        df = get_stock_df(symbol, api_key, time)
        if df is not None:
            st.subheader(f"{symbol} company's {time_period} stock prices")
            st.line_chart(df[['Open', 'High', 'Low', 'Close']])
            st.subheader("Raw Data")
            st.dataframe(df)
    else:
        st.warning("Please select a time interval, stock symbol, and enter your API key.")
