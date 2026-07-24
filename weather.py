from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Richmond"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\*** Get Current Weather ***\n')

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string entered with only spaces, strip removes whitespace
    if not bool(city.strip()):
        city = "Richmond"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)    # pretty print the weather data in a readable format 