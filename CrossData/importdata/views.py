import requests

from rest_framework.response import Response
from rest_framework.views import APIView

# from .models import Game
# from .serializers import GameSerializer

import pandas as pd


class GamesView(APIView):
    '''
        View that calls SteamSpy API
        and return some relevant
        information about a game
        and filter for Null value
    '''
    def get(self, request, format=None):

        games_igdb = self.get_games_igdb()
        games_steam = self.get_games_steam()
        games_twich = self.get_games_twich()
        games_youtube = self.get_games_youtube()

        data = {
            'data1':games_igdb,
            'data2':games_steam,
            'data3':games_twich,
            'data4':games_youtube,
        }

        return Response(data=data)


    def get_games_igdb(self):
        url = 'http://igdbweb:8000/api/get_igdb_games_list/all'
        header = {'Accept': 'application/json'}
        gamedata = requests.get(url, headers=header)
        return gamedata.json()


    def get_games_steam(self):
        url = 'http://steamweb:8000/api/get_steam_games_list/'
        header = {'Accept': 'application/json'}
        gamedata = requests.get(url, headers=header)
        return gamedata.json()


    def get_games_twich(self):
        url = 'http://twitchweb:8000/api/request_stream_list/'
        header = {'Accept': 'application/json'}
        gamedata = requests.get(url, headers=header)
        return gamedata.json()


    def get_games_youtube(self):
        url = 'http://youtubeweb:8000/api/get_youtube_games_list/'
        header = {'Accept': 'application/json'}
        gamedata = requests.get(url, headers=header)
        return gamedata.json()
