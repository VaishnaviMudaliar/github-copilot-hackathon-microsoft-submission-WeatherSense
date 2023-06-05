import folium
import os
import requests
from dotenv import load_dotenv
import webbrowser

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


def display_weather_on_map(latitude, longitude, temperature, weather_description,suggestion,pollution):
    # Create a map centered on the specified location
    map_obj = folium.Map(location=(latitude, longitude), zoom_start=10)

    # Add a marker to the map for the specified location
    popup_text = f"Temperature: {temperature}°C\nWeather Condition: {weather_description}\nClothes to be worn : {suggestion}\nPollution Index : {pollution}"
    folium.Marker(location=(latitude, longitude), popup=popup_text).add_to(map_obj)

    # Display the map
    map_file_path = "weather_map.html"
    map_obj.save(map_file_path)
    return map_file_path

# on the basis of temperature , write a function to suggest what to wear
# if temperature is less than 10 degree celcius , suggest to wear a jacket
# if temperature is between 10 and 20 degree celcius , suggest to wear a sweater
# if temperature is between 20 and 30 degree celcius , suggest to wear a t-shirt
# if temperature is between 30 and 40 degree celcius , suggest to wear a shorts
# if temperature is greater than 40 degree celcius , suggest to wear a cap

def suggest_clothes(temperature):
    suggestion = ""
    if temperature < 10:
        suggestion = "Wear a jacket"
    elif temperature >= 10 and temperature < 20:
        suggestion = "Wear a sweater"
    elif temperature >= 20 and temperature < 30:
        suggestion = "Wear a t-shirt"
    elif temperature >= 30 and temperature < 40:
        suggestion = "Wear a shorts"
    elif temperature >= 40:
        suggestion = "Wear a cap"
    return suggestion



# claculate pollution index on the basis of air quality index
def pollution_index(weather_description):
    pollution_index = ""
    if weather_description == "Clear":
        pollution_index = "0"
    elif weather_description == "Clouds":
        pollution_index = "1"
    elif weather_description == "Rain":
        pollution_index = "2"
    elif weather_description == "Thunderstorm":
        pollution_index = "3"
    elif weather_description == "Drizzle":
        pollution_index = "4"
    elif weather_description == "Snow":
        pollution_index = "5"
    elif weather_description == "Mist":
        pollution_index = "6"
    elif weather_description == "Smoke":
        pollution_index = "7"
    elif weather_description == "Haze":
        pollution_index = "8"
    elif weather_description == "Dust":
        pollution_index = "9"
    elif weather_description == "Fog":
        pollution_index = "10"
    elif weather_description == "Sand":
        pollution_index = "11"
    elif weather_description == "Ash":
        pollution_index = "12"
    elif weather_description == "Squall":
        pollution_index = "13"
    elif weather_description == "Tornado":
        pollution_index = "14"
    return pollution_index

# write a function to suggest user to take precautions on the basis of pollution index
# if pollution index is 0 , suggest to take no precautions
# if pollution index is 1 , suggest to wear a mask
# if pollution index is 2 , suggest to wear a mask and stay indoors
# if pollution index is 3 , suggest to wear a mask and stay indoors
# if pollution index is 4 , suggest to wear a mask and stay indoors
# if pollution index is 5 , suggest to wear a mask and stay indoors
# if pollution index is 6 , suggest to wear a mask and stay indoors
# if pollution index is 7 , suggest to wear a mask and stay indoors
# if pollution index is 8 , suggest to wear a mask and stay indoors
# if pollution index is 9 , suggest to wear a mask and stay indoors
# if pollution index is 10 , suggest to wear a mask and stay indoors
# if pollution index is 11 , suggest to wear a mask and stay indoors
# if pollution index is 12 , suggest to wear a mask and stay indoors
# if pollution index is 13 , suggest to wear a mask and stay indoors
# if pollution index is 14 , suggest to wear a mask and stay indoors

def suggest_precautions(pollution_index):
    suggest_precautions = ""
    if pollution_index == "0":
        suggest_precautions = "No precautions"
    elif pollution_index == "1":
        suggest_precautions = "Wear a mask"
    elif pollution_index == "2":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "3":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "4":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "5":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "6":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "7":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "8":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "9":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "10":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "11":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "12":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "13":
        suggest_precautions = "Wear a mask and stay indoors"
    elif pollution_index == "14":
        suggest_precautions = "Wear a mask and stay indoors"
    return suggest_precautions
        

def main():
    city = input("Enter a city name: ")
    weather_data = fetch_weather_data(city)
    if weather_data.get("cod") == 200:
        air_quality_index = weather_data["main"]["aqi"]
        latitude = weather_data["coord"]["lat"]
        longitude = weather_data["coord"]["lon"]
        temperature = weather_data["main"]["temp"]
        suggestion  = suggest_clothes(temperature)
        pollution = pollution_index(air_quality_index)
        weather_description = weather_data["weather"][0]["description"]
        map_image_path = display_weather_on_map(latitude, longitude, temperature, weather_description,suggestion,pollution)
        print(f"Weather map generated: {map_image_path}")
        webbrowser.open('weather_map.html')
        
    else:
        print("Failed to fetch weather data.")







if __name__ == "__main__":
    main()



