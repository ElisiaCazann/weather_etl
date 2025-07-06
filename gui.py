# streamlit run gui.py
import streamlit as st
from src.etl import get_weather_data, transform_weather_data
import json
from datetime import datetime
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')
if api_key:
    pass
else:
    print("Secret key is missing!")

st.title("Weather Data")
city = st.text_input("Enter city name(s):")
csv_path = "data/weather_history.csv"
cities = [c.strip() for c in city.split(",")]
all_dataframes = []

if st.button("Check"):
    st.write(f"Here's the weatrher in", city.title())
    for city in cities:
        try:
            data = get_weather_data(city, api_key)
            df = transform_weather_data(data)
            df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            all_dataframes.append(df)
            st.dataframe(df)
            #st.write("Data retrieved for", city.title()), " in weather_history.csv"
        except Exception as e:
            st.write(f"Error for '{city}': {e}")







