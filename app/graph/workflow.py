from langgraph.graph import StateGraph
from typing import TypedDict
from app.graph.nodes import (
    fetch_weather_node,
    send_email_node
)
class WeatherState(TypedDict):
    cities: list
    weather_data: list
    email_sent: bool
    

builder = StateGraph(WeatherState)

builder.add_node(
    "fetch_weather",
    fetch_weather_node
)

builder.add_node(
    "send_email",
    send_email_node
)

#Fetch weather
builder.set_entry_point("fetch_weather")

#Connection between fetch_weather and send_email
builder.add_edge(
    "fetch_weather",
    "send_email"
)

builder.set_finish_point("send_email")

graph = builder.compile()