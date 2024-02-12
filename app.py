import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('./notebooks/vehicles_us.csv')  # leer los datos

st.title('Wheel Wonders: Where Every Turn Leads to Your Perfect Pre-Loved Ride')
