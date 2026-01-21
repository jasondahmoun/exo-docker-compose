import os
from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

URL_USERS = os.getenv("URL_USERS")
TOR_CONFIG = os.getenv("TOR_CONFIG")

PROXIES = {
    "http": TOR_CONFIG,
    "https": TOR_CONFIG,
}

@app.get("/api/users")
def users():
    r = requests.get(
        URL_USERS,
        params={"results": 10},
        proxies=PROXIES,
        timeout=20,
    )
    data = r.json()

    return jsonify([
        {
            "nom": f"{u['name']['first']} {u['name']['last']}",
            "photo": u['picture']['large'],
        }
        for u in data["results"]
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)