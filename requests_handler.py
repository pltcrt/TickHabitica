import requests
import json
from config import CONFIG

def get_data():
    response = requests.get(CONFIG["auth"]["url"], headers=CONFIG["auth"]["headers"])
    print("GET Response:", response.json())
    return response.json()

def post_data(payload):
    response = requests.post(CONFIG["post"]["url"], headers=CONFIG["post"]["headers"], json=payload)
    print("POST Sent:", json.dumps(payload, indent=2))
    print("POST Response:", response.json())
    return response.json()