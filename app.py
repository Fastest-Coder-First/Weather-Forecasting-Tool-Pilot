import requests
import json
import sys
from argparse import ArgumentParser


def fetch_weather_data(city):
    """
    Fetches weather data for a given city using OpenWeatherMap API.

    Args:
        city (str): Name of the city.

    Returns:
        dict: Weather data as a dictionary.

    Raises:
        SystemExit: If an error occurs during the API request.
    """
    api_key = "69b96a041d087d878a3f5bc6d466fb60"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    print(url)

    try:
        response = requests.get(url)
        return response.json()
    except:
        print("An error occurred.")
        print("Please check the city name you have entered.")
        print("Please check your internet connection.")
        print("Please try again later.")
        sys.exit(0)


def display_weather_forecast(weather_data):
    """
    Displays the weather forecast for a given city.

    Args:
        weather_data (dict): Weather data as a dictionary.
    """
    city = weather_data['name']
    temperature = weather_data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
    pressure = weather_data['main']['pressure']
    latitude = weather_data['coord']['lat']
    longitude = weather_data['coord']['lon']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print("\nWeather Forecast For {}:".format(city))
    print(f"Temperature: {temperature:.2f} °C")
    print(f"Pressure: {pressure} hPa")
    print(f"Coordinates: {latitude}, {longitude}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")


if __name__ == "__main__":
    parser = ArgumentParser(description="Weather Forecasting Tool")
    parser.add_argument("-c", "--city", dest="city", help="City name", required=True)
    args = parser.parse_args()

    city = args.city

    # Print ASCII art on the CLI using an ASCII shadow font
    print("███████╗ █████╗ ███████╗████████╗███████╗███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗██████╗     ███████╗██╗██████╗ ███████╗████████╗")
    print("██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║██╔══██╗██╔════╝╚══██╔══╝")
    print("█████╗  ███████║███████╗   ██║   █████╗  ███████╗   ██║       ██║     ██║   ██║██║  ██║█████╗  ██████╔╝    █████╗  ██║██████╔╝███████╗   ██║   ")
    print("██╔══╝  ██╔══██║╚════██║   ██║   ██╔══╝  ╚════██║   ██║       ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗    ██╔══╝  ██║██╔══██╗╚════██║   ██║   ")
    print("██║     ██║  ██║███████║   ██║   ███████╗███████║   ██║       ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║    ██║     ██║██║  ██║███████║   ██║   ")

    weather_data = fetch_weather_data(city)
    display_weather_forecast(weather_data)

