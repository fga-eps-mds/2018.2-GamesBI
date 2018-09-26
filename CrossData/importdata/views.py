import requests

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GeneralData
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

        GeneralData.objects.all().delete()
        games_igdb = self.get_games_igdb()
        games_steam = self.get_games_steam()
        games_twich = self.get_games_twich()
        games_youtube = self.get_games_youtube()

        dataFrame_igdb = self.filter_games_igdb(games_igdb)
        dataFrame_steam = self.filter_games_steam(games_steam)
        dataFrame_twich = self.filter_games_twitch(games_twich)
        dataFrame_youtube = self.filter_games_youtube(games_youtube)

        dataframe_all = self.merge_dataFrames(dataFrame_igdb, dataFrame_steam, dataFrame_youtube, dataFrame_twich)
        self.save_games(dataframe_all)

        sucess = {'mensagem':'Importação feita com sucesso!'}
        return Response(data=sucess)


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
        array_id = []
        array_name = []
        array_time_to_beat = []
        array_hypes = []
        array_popularity = []
        array_critics_rating = []
        array_genres = []

        for game in games_igdb:
            array_id.append(game['id'])
            array_name.append(game['name'])
            array_time_to_beat.append(game['time_to_beat'])
            array_hypes.append(game['hypes'])
            array_popularity.append(game['popularity'])
            array_critics_rating.append(game['aggregated_rating'])
            if(len(game['genres']) > 0):
                array_genres.append(game['genres'][0]['name'])
            else:
                array_genres.append(None)

        filtered_game = {
            'id': array_id,
            'name': array_name,
            'time_to_beat': array_time_to_beat,
            'hypes': array_hypes,
            'popularity': array_popularity,
            'critics_rating': array_critics_rating,
            'genres': array_genres
        }
        return pd.DataFrame(filtered_game)


    def filter_games_youtube(self, games_youtube):
        array_id = []
        array_name = []
        array_count_videos = []
        array_count_views = []
        array_count_likes = []
        array_count_dislikes = []
        array_count_comments = []

        for game in games_youtube:
            array_id.append(game['id'])
            array_name.append(game['name'])
            array_count_videos.append(game['count_videos'])
            array_count_views.append(game['count_views'])
            array_count_likes.append(game['count_likes'])
            array_count_dislikes.append(game['count_dislikes'])
            array_count_comments.append(game['count_comments'])

        filtered_game = {
            'id': array_id,
            'name': array_name,
            'count_videos': array_count_videos,
            'count_views': array_count_views,
            'count_likes': array_count_likes,
            'count_dislikes': array_count_dislikes,
            'count_comments': array_count_comments,
        }

        return pd.DataFrame(filtered_game)


    def filter_games_twitch(self, games_twitch):
        array_name = []
        array_views = []

        for game in games_twitch:
            array_name.append(game['game_name'])
            array_views.append(game['total_views'])

        filtered_game = {
            'name': array_name,
            'views': array_views,
        }
        return pd.DataFrame(filtered_game)


    def filter_games_steam(self, games_steam):
        array_id = []
        array_name = []
        array_positive_reviews_steam = []
        array_negative_reviews_steam = []
        array_owners = []
        array_average_forever = []
        array_average_2weeks = []
        array_price = []
        array_languages = []

        for game in games_steam:
            array_id.append(game['id'])
            array_name.append(game['name'])
            array_positive_reviews_steam.append(game['positive_reviews_steam'])
            array_negative_reviews_steam.append(game['negative_reviews_steam'])
            array_owners.append(game['owners'])
            array_average_forever.append(game['average_forever'])
            array_average_2weeks.append(game['average_2weeks'])
            array_price.append(game['price'])
            array_languages.append(game['lenguages'])

        filtered_game = {
            'id': array_id,
            'name': array_name,
            'positive_reviews_steam': array_positive_reviews_steam,
            'negative_reviews_steam': array_negative_reviews_steam,
            'owners': array_owners,
            'average_forever': array_average_forever,
            'average_2weeks': array_average_2weeks,
            'price': array_price,
            'languages_game': array_languages
        }

        return pd.DataFrame(filtered_game)


    def merge_dataFrames(self, frame_igdb, frame_steam, frame_youtube, frame_twich):

        merge_one = pd.merge(frame_igdb, frame_youtube, how='left', on='name')
        merge_two = pd.merge(merge_one, frame_steam, how='left', on='name')
        merge_all = pd.merge(merge_two, frame_twich, how='left', on='name')

        return merge_all


    def valid_nan_values(self, dataframe_all):
        dataframe_all['name'].fillna("", inplace=True)
        dataframe_all['time_to_beat'].fillna(0, inplace=True)
        dataframe_all['hypes'].fillna(0, inplace=True)
        dataframe_all['popularity'].fillna(0, inplace=True)
        dataframe_all['price'].fillna(0, inplace=True)
        dataframe_all['critics_rating'].fillna(0, inplace=True)
        dataframe_all['positive_reviews_steam'].fillna(0, inplace=True)
        dataframe_all['negative_reviews_steam'].fillna(0, inplace=True)
        dataframe_all['owners'].fillna(0, inplace=True)
        dataframe_all['average_forever'].fillna(0, inplace=True)
        dataframe_all['average_2weeks'].fillna(0, inplace=True)
        dataframe_all['genres'].fillna("", inplace=True)
        dataframe_all['languages_game'].fillna("", inplace=True)
        dataframe_all['count_videos'].fillna(0, inplace=True)
        dataframe_all['count_views'].fillna(0, inplace=True)
        dataframe_all['count_likes'].fillna(0, inplace=True)
        dataframe_all['count_dislikes'].fillna(0, inplace=True)
        dataframe_all['count_comments'].fillna(0, inplace=True)
        dataframe_all['views'].fillna(0, inplace=True)

        return dataframe_all

    def save_games(self, dataframe_all):
        number_rows = dataframe_all.count()['name']
        dataframe = self.valid_nan_values(dataframe_all)
        count = 0
        while count < number_rows:
            game = dataframe.loc[count]
            new_game = GeneralData(
                # id_igdb
            	# id_steam
            	# id_twitch
            	name=str(game['name']),
            	time_to_beat=float(game['time_to_beat']),
            	hypes=int(game['hypes']),
            	popularity=float(game['popularity']),
            	critics_rating=float(game['critics_rating']),
            	genres=str(game['genres']),
            	positive_reviews_steam=int(game['positive_reviews_steam']),
            	negative_reviews_steam=int(game['negative_reviews_steam']),
            	owners=int(game['owners']),
            	average_forever=int(game['average_forever']),
            	average_2weeks=int(game['average_2weeks']),
            	price=int(game['price']),
            	languages_game=str(game['languages_game']),
            	count_videos=int(game['count_videos']),
            	count_views=int(game['count_views']),
            	count_likes=int(game['count_likes']),
            	count_dislikes=int(game['count_dislikes']),
            	count_comments=int(game['count_comments']),
            	view_count=int(game['views'])
            	# follows
            	# language
            	# started_at
            	# type
            	# viewer_count
            )
            new_game.save()
            print("JOGO SALVO " + new_game.name)
            print("----------------------")
            print("----------------------")
            print("----------------------")
            count+=1
