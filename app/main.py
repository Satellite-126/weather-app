from fastapi import FastAPI
from app.graph.workflow import graph
from app.services.scheduler_service import scheduler
from app.db import engine
from app.models import Base

from dotenv import load_dotenv

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Weather API Running"}

@app.get("/run-weather")

def run_weather():

    result = graph.invoke({
        "cities": [
            "San Francisco",
            "Manosque",
            "Warsaw"
        ]
    })

    return {
        "status": "success",
        "data": result
    }