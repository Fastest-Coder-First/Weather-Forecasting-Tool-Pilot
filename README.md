# Weather Forecasting Tool
![Python Version](https://img.shields.io/badge/python-3.9-blue.svg) ![CLI](https://img.shields.io/badge/CLI-yes-brightgreen.svg) ![Documentation](https://img.shields.io/badge/documentation-yes-brightgreen.svg) ![Code Quality](https://img.shields.io/badge/code%20quality-A-brightgreen.svg) ![Code Linter](https://img.shields.io/badge/code%20linter-passing-brightgreen.svg)


This is a simple command line tool to fetch and display the weather forecast for a given city.

# Architecture Flow

The Weather Forecasting Tool follows a simple architectural flow to fetch and display the weather forecast for a given city. Here's an overview of the flow:

1. **Command Line Interface (CLI)**: The tool is invoked through a command line interface, where the user provides the desired city name as a command line argument.

2. **API Integration**: The tool integrates with the OpenWeatherMap API to fetch weather data for the specified city. It uses the `requests` library to send a GET request to the API endpoint, passing the city name and API key as parameters.

3. **Data Parsing**: The response from the API is received in JSON format. The tool parses the JSON data to extract the required weather features such as temperature, pressure, humidity, wind speed, and coordinates.

4. **Displaying Weather Forecast**: The extracted weather features are displayed on the command line, providing the user with the current weather forecast for the specified city.

5. **Dependencies**: The tool may have dependencies on external libraries or modules. Ensure that the necessary dependencies are installed before running the tool. Refer to the Installation section in the README for instructions on installing dependencies.

This architectural flow demonstrates the simplicity and effectiveness of the Weather Forecasting Tool in providing real-time weather information to users.


## Usage

```bash
python app.py --city <city_name>
```

## Example

```bash
python app.py --city London
```

## Output

![https://i.imgur.com/Lz2LgCX.png](https://i.imgur.com/Lz2LgCX.png)

```bash
Weather Forecast For London:
```

```bash
Temperature: 16.00 °C
Pressure: 1016 hPa
Coordinates: 51.51, -0.13
Humidity: 77%
Wind Speed: 4.63 m/s
```

## Command Line Arguments

The tool accepts the following command line arguments:

```bash
usage: app.py [-h] -c CITY
```

# Weather Forecasting Tool

```bash
optional arguments:
  -h, --help            show this help message and exit
  -c CITY, --city CITY  City name
```

# Installation
Clone the repository:

```bash
git clone https://github.com/Fastest-Coder-First/Weather-Forecasting-Tool-Pilot
```

Change the working directory:

```bash 
cd Weather-Forecasting-Tool-Pilot

```

# API Reference :- 

[OpenWeatherMap API](https://openweathermap.org/api)

# Acknowledgements

Special thanks to [Microsoft Azure](https://azure.microsoft.com/) ❤️

[FastestCoderFirst](https://www.fastestcoderfirst.com/) ❤️

[ID8NXT](https://id8nxt.com/) ❤️

ASCII Art Generator for the ASCII art. GitHub and GitHub Copilot for the code 
