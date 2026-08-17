import requests

API_KEY = "197b34523d9a90d532c77185f10b8064"

city = input("Enter city: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

data = response.json()

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]

condition = data["weather"][0]["description"]

wind_speed = data["wind"]["speed"]

city_name = data["name"]

print()
print("Weather in", city_name)
print("Temperature:", temperature, "°C")
print("Feels like:", feels_like, "°C")
print("Humidity:", humidity, "%")
print("Condition:", condition)
print("Wind speed:", wind_speed, "m/s")

