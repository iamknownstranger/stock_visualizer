from datetime import datetime
import pandas as pd
import streamlit as st
from nsepy import get_history
import plotly.graph_objects as go

st.title('Stock Visualizer')
with st.form(key='form'):
    symbol = st.text_input('Enter the Symbol of the stock to visalize')
    start_date = st.date_input('Select the start date')
    end_date = st.date_input('Select the end date')

    visualize_button = st.form_submit_button('Visualize')

    if visualize_button:
        
        data = get_history(symbol=symbol,
                        start=start_date,
                        end=end_date)

        if not data.empty:
            
            chart = go.Figure(data=[go.Candlestick(x=data.index,
                        open=data.Open,
                        high=data.High,
                        low=data.Low,
                        close=data.Close)])

            st.subheader("Historical Data")
            st.dataframe(data)
            st.subheader("Chart")
            st.plotly_chart(chart)

