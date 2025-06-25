import requests
import pandas as pd

def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}")


def transform_weather_data(json_data):
    transformed = {
        "city": json_data["name"],
        "country": json_data["sys"]["country"],
        "temperature": json_data["main"]["temp"],
        "humidity": json_data["main"]["humidity"],
        "weather": json_data["weather"][0]["main"],
        "description": json_data["weather"][0]["description"],
        "wind_speed": json_data["wind"]["speed"]
    }
    df = pd.DataFrame([transformed]) #dictionary
    return df
