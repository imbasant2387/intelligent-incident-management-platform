from fastapi import FastAPI
from typing import Dict

app = FastAPI()

incidents = []

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "incident-service"
    }

@app.get("/incidents")
def get_incidents():
    return incidents

@app.post("/webhook")
def receive_alert(payload: Dict):

    incidents.append(payload)

    return {
        "message": "incident created",
        "incident_count": len(incidents)
    }
