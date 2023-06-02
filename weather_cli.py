import folium
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenWeatherMap API configuration
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"



def fetch_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # You can change the units to imperial if desired
    }
    response = requests.get(API_BASE_URL, params=params, timeout=5)
    return response.json()


def display_weather_on_map(latitude, longitude, temperature, weather_description):
    # Create a map centered on the specified location
    map_obj = folium.Map(location=(latitude, longitude), zoom_start=10)

    # Add a marker to the map for the specified location
    popup_text = f"Temperature: {temperature}°C\nWeather Condition: {weather_description}"
    folium.Marker(location=(latitude, longitude), popup=popup_text).add_to(map_obj)

    # Display the map
    map_file_path = "weather_map.html"
    map_obj.save(map_file_path)
    return map_file_path



def main():
    city = input("Enter a city name: ")
    weather_data = fetch_weather_data(city)
    if weather_data.get("cod") == 200:
        latitude = weather_data["coord"]["lat"]
        longitude = weather_data["coord"]["lon"]
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        map_image_path = display_weather_on_map(latitude, longitude, temperature, weather_description)
        print(f"Weather map generated: {map_image_path}")
    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    main()




