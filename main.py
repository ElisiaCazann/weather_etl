from src.etl import get_weather_data, transform_weather_data
import json
from datetime import datetime
import os

api_key = "f9a27b6af310dd37bc23b39590f7822f"
city = input("Enter city name: ")
csv_path = "data/weather_history.csv"
cities = [c.strip() for c in city.split(",")]
all_dataframes = []

for city in cities:
    try:
        data = get_weather_data(city, api_key)
        df = transform_weather_data(data)
        df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        all_dataframes.append(df)
        print("Data retrieved for", city.title())
    except Exception as e:
        print(f"Error for '{city}': {e}")

# If we have valid data, append to CSV
if all_dataframes:
    from pandas import concat

    full_df = concat(all_dataframes, ignore_index=True)
    print("\n Weather Data:")
    print(full_df)

    file_exists = os.path.isfile(csv_path)
    full_df.to_csv(csv_path, mode="a", header=not file_exists, index=False)
    print(f" Data appended to: {csv_path}")
else:
    print("No valid data to save.")