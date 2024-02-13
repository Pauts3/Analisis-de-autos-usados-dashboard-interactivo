import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

car_data = pd.read_csv('vehicles_us.csv')

obj_columns = ['model', 'condition', 'fuel', 'transmission', 'type']

st.title('Wheel Wonders: Where Every Turn Leads to Your Perfect Pre-Loved Ride')

models_by_year = car_data.groupby('model')['model_year'].unique()

if st.checkbox('Cars models'):
    st.subheader('Some of our models by year:')
    st.write(models_by_year.sample(20))


hist_button = st.button("Prices' Histogram")

if hist_button:
    st.header("Wheel Wonders' prices")
    st.write(
        "Check out our Wheel Wonders' prices!")
    fig1 = px.histogram(car_data, x='price', labels={
        'price': 'USD price'})
    st.plotly_chart(fig1)

scatter_button = st.button("Cars' condition chart")

if scatter_button:
    st.header('How Pre-loved are the Wheel Wonders')
    st.write(
        "Compare the conditions of each car depending on the model's year and odometer readings.")
    fig2 = px.scatter(car_data, x='model_year',
                      y='odometer', color='condition', labels={'model_year': 'Model year', 'odometer': 'Odometer reading'})
    st.plotly_chart(fig2)

st.header('Get to know a little more about the Wheel Wonders')

st.write("Here is an interactive bar chart to learn more about our pre-loved cars:")

col1, col2 = st.columns([0.25, 0.75])

with col1:
    c_axis = st.selectbox('Color:', obj_columns)

with col2:
    fig3, ax = st.bar_chart(car_data, x='model_year',
                            y='price', color=c_axis, use_container_width=True)
    st.plotly_chart(fig3)
