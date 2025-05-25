import requests

API_KEY = "3d3ad06e30b8400f4617d63d6e249038"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric' 
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"City '{city_name}' not found. Please check the city name and try again.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

def display_weather(data):
    if data:
        city = data.get('name')
        country = data['sys'].get('country')
        weather_desc = data['weather'][0].get('description').capitalize()
        temperature = data['main'].get('temp')
        humidity = data['main'].get('humidity')
        wind_speed = data['wind'].get('speed')

        print(f"\nWeather in {city}, {country}:\n")
        print(f"Condition: {weather_desc}\n")
        print(f"Temperature: {temperature}°C\n")
        print(f"Humidity: {humidity}%\n")
        print(f"Wind Speed: {wind_speed} m/s\n")
    else:
        print("No weather data to display.")

def main():
    print("\n\n=== Weather Forecast ===\n\n")
    city_name = input("Enter name of the city: ").strip()
    if not city_name:
        print("City name cannot be empty. Please try again.")
        return
    weather_data = get_weather(city_name)
    display_weather(weather_data)

if __name__ == "__main__":
    main()