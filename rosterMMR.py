from app.classes.Player import Player
import json
from dotenv import load_dotenv
import os
import requests as req
from urllib import parse
import pandas as pd

# TO USE:
    # Populate ./data/rawbattletags.csv with desired battletags
        # Line 1 should always read "Name"
    # Program will output to ./results/results.csv

data = pd.read_csv("./data/rawbattletags.csv")
players = []
output = []

# create list of Players; remove whitespace from battletags
    # Player - custom class containing various attributes.  Planning to build that out more.
for label, content in data.items():
    if label == "Name":
        pandaplayers = content.to_list()
        for player in pandaplayers:
            players.append(Player(battletag = player.strip()))

game_types = [
    "Storm League",
    "Quick Match"
]

load_dotenv()
TOKEN = os.getenv('HEROES_PROFILE_TOKEN')
API_URL = os.getenv('API_URL')
OPEN_API_URL = os.getenv('OPEN_API_URL')

hero_url = '{api_url}/Player?api_token={token}&mode=json&battletag={parsed_battletag}&region=1'
# https://api.heroesprofile.com/docs/1.0/Player

hero_mmr_url = '{api_url}/Player/MMR?api_token={token}&mode=json&battletag={parsed_battletag}&region=1&game_type={game_type}'
# https://api.heroesprofile.com/docs/1.0/Player/MMR

for player in players:

    # remove hash symbol from battletag so URL can use it
    player.set_attr(
        parsed_battletag = parse.quote(str(player.battletag))
    )

    # get account level and HP URL
    url = hero_url.format(
        api_url = API_URL,
        token = TOKEN,
        parsed_battletag = player.parsed_battletag
        )
    try:
        res = req.get(url)
        if res.status_code == 200:
            player_content = json.loads(res.content)
            if type(player_content) == dict:
                stats = player_content
                player.set_attr(
                    account_level = stats['account_level'],
                    hp_url = stats['profile']
                )
        else:
            player.set_attr(
                account_level = "API ERROR",
                hp_url = "API ERROR"
            )
    except:
        player.set_attr(
            account_level = "EXCEPTION ERROR",
            hp_url = "EXCEPTION ERROR"
        )

    # get SL, QM MMR and # of games played
    mode_quantity = len(game_types)
    MMR = [0]*mode_quantity
    games_played = [0]*mode_quantity
        
    for x in range(mode_quantity):    
        url = hero_mmr_url.format(
            api_url = API_URL,
            token = TOKEN,
            parsed_battletag = player.parsed_battletag,
            game_type = game_types[x]
            )
        try:
            res = req.get(url)
            if res.status_code == 200:
                hero_mmr_content = json.loads(res.content)
                if type(hero_mmr_content[str(player.battletag)]) == dict:
                    stats = hero_mmr_content[str(player.battletag)][str(game_types[x])]
                    MMR[x] = stats['mmr']
                    games_played[x] = stats['games_played']
            else:
                MMR[0] = "API ERROR"
                games_played[0] = "API ERROR"
                MMR[1] = "API ERROR"
                games_played[1] = "API ERROR"
        except:
            MMR[0] = "EXCEPTION ERROR"
            games_played[0] = "EXCEPTION ERROR"
            MMR[1] = "EXCEPTION ERROR"
            games_played[1] = "EXCEPTION ERROR"
    output_text = [str(player.battletag),str(player.account_level),str(MMR[0]),str(games_played[0]),str(MMR[1]),str(games_played[1]),str(player.hp_url)]
    print(output_text)
    output.append(output_text)

df = pd.DataFrame(data = output, columns = ['Battletag', 'Account Level', 'SL MMR', '# SL Games', 'QM MMR', '# QM Games', 'Link'])
df = df.to_csv(index = False)

f = open('./results/results.csv','a', newline = '', encoding='utf8')
f.write(df)
f.close()
