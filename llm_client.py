
import requests

def generate_response(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }

    response = requests.post(url, json=payload, timeout=180)
    response.raise_for_status()

    return response.json()["response"]
