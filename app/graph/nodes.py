from app.services.weather_service import get_weather
from app.services.email_service import (
    generate_email_html,
    send_email
)

from app.db import SessionLocal
from app.models import WeatherLog

#Fetch weather
def fetch_weather_node(state):

    cities = state["cities"]

    results = []

    db = SessionLocal()

    for city in cities:

        weather = get_weather(city)

        results.append(weather)

        log = WeatherLog(
            city=weather["city"],
            temperature=weather["temperature"],
            condition=weather["condition"],
            humidity=weather["humidity"],
            feel = weather["feel"]
        )

        db.add(log)

    db.commit()

    print("Data Saved!")

    state["weather_data"] = results

    return state

#Email send
def send_email_node(state):

    weather_data = state["weather_data"]

    html = generate_email_html(weather_data)

    send_email(
        "jcbpilkington@gmail.com",
        html
    )

    state["email_sent"] = True

    return state