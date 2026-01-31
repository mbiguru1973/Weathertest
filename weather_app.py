import requests

def get_weather_data(city_name, api_key):
    try:
        # Base URL for the OpenWeatherMap API
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # Parameters for the API call
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric"  # Use "imperial" for Fahrenheit
        }
        
        # Make the GET request to the API
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract required weather information
        city = data.get("name")
        country = data["sys"]["country"]
        temperature_min = data["main"]["temp_min"]
        temperature_max = data["main"]["temp_max"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        
        # Return the formatted weather information
        return {
            "city": city,
            "country": country,
            "temperature_min": temperature_min,
            "temperature_max": temperature_max,
            "humidity": humidity,
            "forecast": weather_description
        }
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Main program
if __name__ == "__main__":
    # Replace with your own OpenWeatherMap API Key
    API_KEY = "your_openweathermap_api_key_here"
    
    city = input("Enter the name of the city: ")
    
    # Get weather data
    weather = get_weather_data(city, API_KEY)
    
    if weather:
        print("\nWeather Information:")
        print(f"City: {weather['city']}, {weather['country']}")
        print(f"Min Temperature: {weather['temperature_min']}°C")
        print(f"Max Temperature: {weather['temperature_max']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Forecast: {weather['forecast']}")
    else:
        print("Could not retrieve weather data. Please try again.")