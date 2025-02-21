import os
import requests
import datetime


# Replace with your Lichess API token
API_TOKEN = os.environ["API_TOKEN"]


def main(res):
    # Get the current date and time in the server location
    now = datetime.datetime.now()

    # Start the tournament at (1am in Frankfurt):(8am in Caracas)
    start_time = now + datetime.timedelta(hours=8)

    # Tournament parameters
    tournament_data = {
        "name": "Torneo de los viernes",
        "clockTime": 5,  # 5 minutes per player
        "clockIncrement": 3,  # 0 second increment
        "minutes": 90,  # Tournament duration in minutes
        "startDate": int(start_time.timestamp() * 1000),  # Start date in milliseconds
        "variant": "standard",  # Game variant
        "rated": False,  # Rated tournament
    }

    # API endpoint to create a tournament
    url = "https://lichess.org/api/tournament"

    # Headers with authorization
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    # Make the request to create the tournament
    response = requests.post(url, json=tournament_data, headers=headers)

    if response.status_code == 200:
        tournament_id = response.json().get("id")
        tournament_url = f"https://lichess.org/tournament/{tournament_id}"
        return res.json({"tournament_url": tournament_url})
    else:
        print("Failed to create tournament.")
        print("Response:", response.text)
        return None
