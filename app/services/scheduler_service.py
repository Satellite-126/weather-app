from apscheduler.schedulers.background import BackgroundScheduler
from app.graph.workflow import graph

scheduler = BackgroundScheduler()

def run_daily_job():

    print("Running Daily Weather Job!")

    graph.invoke({
        "cities": [
            "San Francisco",
            "Warsaw",
            "Manosque"  
        ]
    })

scheduler.add_job(
    run_daily_job,
    trigger="cron",
    hour=8,
    minute=0
)

scheduler.start()