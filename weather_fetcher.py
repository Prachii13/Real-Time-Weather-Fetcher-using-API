import requests

API_KEY = "your_openweathermap_api_key"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"\n🌆 Weather in {data['name']}, {data['sys']['country']}")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌤️ Condition: {data['weather'][0]['description'].capitalize()}")
    else:
        print("❌ City not found or API error.")

def main():
    print("🌦️ Real-Time Weather Fetcher")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
