import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

car_data = pd.read_csv('./notebooks/vehicles_us.csv')

num_columns = ['price', 'model_year']

obj_columns = ['model', 'condition', 'fuel', 'transmission', 'type']

st.title('Wheel Wonders: Where Every Turn Leads to Your Perfect Pre-Loved Ride')

models_by_year = car_data.groupby('model')['model_year'].unique()

models_by_price = car_data.groupby('model')['price'].mean()

if st.checkbox('Cars models'):
    st.subheader('Some of our models by year')
    st.write(models_by_year.sample(20))


hist_button = st.button("Prices' Histogram")

if hist_button:
    st.header('Wheel Wonders prices')
    st.write(
        'Check out our Wheel Wonders prices')
    fig1 = px.histogram(car_data, x='price', labels={
        'price': 'USD prices'})
    st.plotly_chart(fig1)

scatter_button = st.button("Condition Histogram")

if scatter_button:
    st.header('How Pre-loved are the Wheel Wonders')
    st.write("Check out the cars' condition")
    scatter_fig = px.scatter(car_data, x='model_year',
                             y='odometer', color='condition')
    st.plotly_chart(scatter_fig)

st.header('How Pre-loved are the Wheel Wonders')

st.write("Check out the cars' condition by year")

col1, col2 = st.columns([0.25, 0.75])

with col1:

    x_axis = st.selectbox('X axis:', 'num_columns', index=0)

    y_axis = st.selectbox('Y axis:', num_columns, index=1)

    c_axis = st.selectbox('Color:', obj_columns)

with col2:
    fig2, ax = st.bar_chart(car_data, x=x_axis, y=y_axis, color=c_axis)
    st.plotly_chart(fig2)
