import requests
import json
import sys

def get_weather(city):
    api_key = "fbcdf2a5a3833ff7e69f86c64890865e"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful API calls
        weather_data = response.json()
        
        # Parse the weather data
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        
        return f"The current temperature in {city} is {temperature}°C with {weather_description}."
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a city name as an argument.")
        sys.exit(1)
    
    city_name = " ".join(sys.argv[1:])
    print(get_weather(city_name))
