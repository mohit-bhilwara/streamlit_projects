import streamlit as st
import pandas as pd
import yfinance as yf


st.write("""
# Simple Stock Price App

Show the stock ***closing price*** and ***volume*** of Tesla

"""
)

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)


tickerDf = tickerData.history(period='1d',start='2010-5-31',end='2020-5-31')


st.line_chart(tickerDf.Close)
st.write('---')
st.line_chart(tickerDf.Volume)

