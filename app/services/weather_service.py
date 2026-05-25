import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):

    
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url)

    data = response.json()

    print(data)

    #Handle Errors
    if response.status_code != 200:
        return {
            "city": city,
            "temperature": 0,
            "condition": "Unknown",
            "humidity": 0,
            "feel": "Invalid city"
        }

    return {
    "city": city,
    "temperature": data["main"]["temp"],
    "condition": data["weather"][0]["main"],
    "humidity": data["main"]["humidity"],
    "feel": get_weather_feeling(
        data["main"]["temp"],
        data["weather"][0]["main"]
    )
}


#Feeling Function
def get_weather_feeling(temp, condition):

    condition = condition.lower()

    if "snow" in condition:
        return "Snowy and freezing"

    elif "rain" in condition:

        if temp < 10:
            return "Cold and rainy"

        return "Rainy"

    elif "cloud" in condition:

        if temp > 25:
            return "Warm and cloudy"

        return "Cloudy"

    elif "clear" in condition:

        if temp >= 35:
            return "Boiling sunny weather"

        elif temp >= 28:
            return "Very hot and sunny"

        elif temp >= 22:
            return "Warm and sunny"

        elif temp >= 15:
            return "Cool and sunny"

        elif temp >= 5:
            return "Cold but clear"

        else:
            return "Freezing clear weather"

    else:

        if temp >= 35:
            return "Boiling hot"

        elif temp >= 28:
            return "Very hot"

        elif temp >= 22:
            return "Warm"

        elif temp >= 15:
            return "Cool"

        elif temp >= 5:
            return "Cold"

        else:
            return "Freezing"