from sqlalchemy import Column, String, Float, Integer
from app.db import Base
import uuid

class WeatherLog(Base):
    __tablename__ = "weather_logs"

    id = Column(String, primary_key=True,
                default=lambda: str(uuid.uuid4()))

    city = Column(String)
    temperature = Column(Float)
    condition = Column(String)
    humidity = Column(Integer)
    feel = Column(String)