import requests
import pandas as pd
from model import model

def get_information(token, tag):
    api_key = str(token)
    player_tag = tag.strip("#")

    def get_player_data(player_tag):
        url = f"https://api.brawlstars.com/v1/players/%23{player_tag}"
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")

    player_data = get_player_data(player_tag)

    output = open("output.txt", "w", encoding="utf-8")
    if player_data:
        df = pd.json_normalize(player_data)

        expLevel = player_data['expLevel']

        brawlers = player_data['brawlers']
        power_sum = sum(1 for brawler in brawlers if brawler.get('power') == 11)
        power_score = power_sum / 84

        predicted_trophies = model(expLevel, power_score)

        output.write(f"Name: {df['name'][0]}\nTrophies: {df['trophies'][0]}\nPower Score: {power_score}\nExp Level: {expLevel}\nPredicted Trophies: {predicted_trophies}")
    
    else:
        output.write("Failed to fetch player data.")


