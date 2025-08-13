import numpy as np
import pandas as pd
import random
import time
from unidecode import unidecode
import requests
requests.get('https://stats.nba.com', verify=False)  # Disables SSL verification
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from nba_api.stats.static import teams

# Ask for player name
player_name = input("Enter NBA player's name: ")

# Find the player ID
nba_players = players.get_players()
player = next((p for p in nba_players if p['full_name'].lower() == player_name.lower()), None)

if player:
    player_id = player['id']

    # Get player stats
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    stats_df = career_stats.get_data_frames()[0]
    df = career_stats.get_data_frames()[0]

    print(stats_df)
    df['PTS_PER_GAME'] = df['PTS'] / df['GP']
    print(df[['SEASON_ID', 'PTS_PER_GAME']]) 
else:
    print("Player not found. Make sure you entered the full name correctly.")

# career = playercareerstats.PlayerCareerStats(player_id='203999')
# response = career.get_data_frames()[0]
# print(response)

nba_teams = teams.get_teams()
print("Number of teams fetched: {}".format(len(nba_teams)))
nba_teams[:3]

nba_players = players.get_players()
print("Number of players fetched: {}".format(len(nba_players)))
nba_players[:]



# df = career_stats.get_data_frames()[0]
# # Calculate points per game 
# df['PTS_PER_GAME'] = df['PTS'] / df['GP']
# print(df[['SEASON_ID', 'PTS_PER_GAME']])