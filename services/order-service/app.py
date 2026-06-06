from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "order-service"
    }

@app.get("/order")
def order():

    user_response = requests.get(
        "http://user-service:8000/health",
        timeout=5
    )

    return {
        "order_id": 1001,
        "user_service_response": user_response.json()
    }
