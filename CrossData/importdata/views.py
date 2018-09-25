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

        dataFrame_igdb = self.filter_games_igdb(games_igdb)
        dataFrame_steam = self.filter_games_steam(games_steam)
        dataFrame_twich = self.filter_games_twitch(games_twich)
        dataFrame_youtube = self.filter_games_youtube(games_youtube)

        dataframe_all = self.merge_dataFrames(dataFrame_igdb, dataFrame_steam, dataFrame_youtube, dataFrame_twich)
        print(dataframe_all)
        return Response(data=dataFrame_steam )


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


    def filter_games_igdb(self, games_igdb):
        games_list = []
        for game in games_igdb:
            genres = game['genres']
            genero = ""
            for genre in genres:
                genero = genre['name']
                break

            filtered_game = {
                'name': [game['name']],
                'time_to_beat': [game['time_to_beat']],
                'popularity': [game['popularity']],
                'critics_rating': [game['aggregated_rating']],
                'genres': genero
            }
            games_list.append(pd.DataFrame(filtered_game))

        return pd.concat(games_list)


    def filter_games_youtube(self, games_youtube):
        games_list = []
        for game in games_youtube:
            filtered_game = {
                'name': [game['name']],
                'count_videos': [game['count_videos']],
                'count_views': [game['count_views']],
                'count_likes': [game['count_likes']],
                'count_dislikes': [game['count_dislikes']],
                'count_comments': [game['count_comments']],
                'count_favorites': [game['count_favorites']]
            }
            games_list.append(pd.DataFrame(filtered_game))

        return pd.concat(games_list)


    def filter_games_twitch(self, games_twitch):
        games_list = []
        for game in games_twitch:
            filtered_game = {
                'name': [game['game_name']],
                'language': [game['language']],
                'started_at': [game['started_at']],
                'type': [game['type']],
                'viewer_count': [game['viewer_count']]
            }
            games_list.append(pd.DataFrame(filtered_game))

        return pd.concat(games_list)


    def filter_games_steam(self, games_steam):
        games_list = []
        for game in games_steam:
            filtered_game = {
                'name': [game['name']],
                'positive_reviews_steam': [game['positive_reviews_steam']],
                'negative_reviews_steam': [game['negative_reviews_steam']],
                'owners': [game['owners']],
                'average_forever': [game['average_forever']],
                'average_2weeks': [game['average_2weeks']],
                'price': [game['price']],
                'lenguages': None
            }
            games_list.append(pd.DataFrame(filtered_game))

        return pd.concat(games_list)


    def merge_dataFrames(self, frame_igdb, frame_steam, frame_youtube, frame_twitch):

        merge_youtube_steam = pd.merge(frame_youtube, frame_steam, how='outer', on='name')
        merge_igdb_twitch = pd.merge(frame_igdb, frame_twitch, how='outer', on='name')
        merge_all = pd.merge(merge_youtube_steam, merge_igdb_twitch, how='outer', on='name')
        return merge_all
