import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

st.write("""
# Simple Stock Price App

Show the stock ***closing price*** and ***volume*** of Tesla

"""
)

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)
# data = pd.read_csv(tickerData)

tickerDf = tickerData.history(period='1d',start='2010-5-31',end='2020-5-31')
# import plotly.graph_objects as go

# fig = go.Figure()
# fig.add_trace(go.Candlestick(x=tickerData[‘DateTime’], 
#                                           open=tickerData[‘Open’],
#                                           high=tickerData[‘High’],
#                                           low=dataf[‘Low’],
#                                           close=tickerData[‘Close’]) )

# st.plotly_chart(fig)

st.line_chart(tickerDf.Close)
st.write('---')
st.line_chart(tickerDf.Volume)
# st.plotly_chart(fig)
