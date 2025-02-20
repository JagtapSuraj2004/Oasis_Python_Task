import requests

def get_weather(city):
    api_key = "e55cc0fb5647829198c30f31c27313a7"  # Replace with your actual OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != 200:
            print(f"Error: {data['message']}")
        else:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            print(f"Weather in {city}: {weather}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)