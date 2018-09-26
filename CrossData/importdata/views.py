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
        # games_twich = self.get_games_twich()
        games_youtube = self.get_games_youtube()

        dataFrame_igdb = self.filter_games_igdb(games_igdb)
        dataFrame_steam = self.filter_games_steam(games_steam)
        # dataFrame_twich = self.filter_games_twitch(games_twich)
        dataFrame_youtube = self.filter_games_youtube(games_youtube)

        dataframe_all = self.merge_dataFrames(dataFrame_igdb, dataFrame_steam, dataFrame_youtube)
        self.save_games(dataframe_all)

        return Response(data=games_igdb )


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
        array_name = []
        array_time_to_beat = []
        array_hypes = []
        array_popularity = []
        array_critics_rating = []
        array_genres = []

        for game in games_igdb:
            array_name.append(game['name'])
            array_time_to_beat.append(game['time_to_beat'])
            array_hypes.append(game['hypes'])
            array_popularity.append(game['popularity'])
            array_critics_rating.append(game['aggregated_rating'])
            # array_genres.append(game['genres'][0]['name'])

        filtered_game = {
            'name': array_name,
            'time_to_beat': array_time_to_beat,
            'hypes': array_hypes,
            'popularity': array_popularity,
            'critics_rating': array_critics_rating
            # 'genres': array_genres
        }
        return pd.DataFrame(filtered_game)


    def filter_games_youtube(self, games_youtube):
        array_name = []
        array_count_videos = []
        array_count_views = []
        array_count_likes = []
        array_count_dislikes = []
        array_count_comments = []

        for game in games_youtube:
            array_name.append(game['name'])
            array_count_videos.append(game['count_videos'])
            array_count_views.append(game['count_views'])
            array_count_likes.append(game['count_likes'])
            array_count_dislikes.append(game['count_dislikes'])
            array_count_comments.append(game['count_comments'])

        filtered_game = {
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
        array_language = []
        array_started_at = []
        array_type = []
        array_viewer_count = []

        for game in games_twitch:
            array_name.append(game['game_name'])
            array_language.append(game['language'])
            array_started_at.append(game['started_at'])
            array_type.append(game['type'])
            array_viewer_count.append(game['viewer_count'])

        filtered_game = {
            'name': array_name,
            'language': array_language,
            'started_at': array_started_at,
            'type': array_type,
            'viewer_count': array_viewer_count
        }

        return pd.DataFrame(filtered_game)


    def filter_games_steam(self, games_steam):
        array_name = []
        array_positive_reviews_steam = []
        array_negative_reviews_steam = []
        array_owners = []
        array_average_forever = []
        array_average_2weeks = []
        array_price = []
        # array_average_forever = []

        for game in games_steam:
            array_name.append(game['name'])
            array_positive_reviews_steam.append(game['positive_reviews_steam'])
            array_negative_reviews_steam.append(game['negative_reviews_steam'])
            array_owners.append(game['owners'])
            array_average_forever.append(game['average_forever'])
            array_average_2weeks.append(game['average_2weeks'])
            array_price.append(game['price'])

        filtered_game = {
            'name': array_name,
            'positive_reviews_steam': array_positive_reviews_steam,
            'negative_reviews_steam': array_negative_reviews_steam,
            'owners': array_owners,
            'average_forever': array_average_forever,
            'average_2weeks': array_average_2weeks,
            'price': array_price
            # 'lenguages': None
        }

        return pd.DataFrame(filtered_game)


    def merge_dataFrames(self, frame_igdb, frame_steam, frame_youtube):

        merge_one = pd.merge(frame_igdb, frame_youtube, how='left', on='name')
        merge_all = pd.merge(merge_one, frame_steam, how='left', on='name')
        # merge_all = pd.merge(merge_two, frame_youtube, how='left', on='name')

        return merge_all


    def valid_nan_values(self, serie):
        count = 0
        number_sections = serie.count()
        while count < number_sections:
            if (str(serie[count]) == 'nan'):
                serie.at[0] = Null

    def save_games(self, dataframe_all):
        number_rows = dataframe_all.count()['name']
        count = 0
        while count < number_rows:
            game = dataframe_all.loc[count]
            print('nome: ' + str(game.name))
            print('time_to_beat: ' + str(game.time_to_beat))
            print('hypes: ' + str(game.hypes))
            print('popularity: ' + str(game.popularity))
            print('critics_rating: ' + str(game.critics_rating))
            print('positive_reviews_steam: ' + str(game.positive_reviews_steam))
            print('negative_reviews_steam: ' + str(game.negative_reviews_steam))
            print('owners: ' + str(game.owners))
            print('average_forever: ' + str(game.average_forever))
            print('average_2weeks: ' + str(game.average_2weeks))
            print('price: ' + str(game.price))
            print('count_videos: ' + str(game.count_videos))
            print('count_views: ' + str(game.count_views))
            print('count_likes: ' + str(game.count_likes))
            print('count_dislikes: ' + str(game.count_dislikes))
            print('count_comments: ' + str(game.count_comments))

            new_game = GeneralData(
                # id_igdb
            	# id_steam
            	# id_twitch
            	name=str(game.name),
            	time_to_beat=float(game.time_to_beat),
            	# hypes=int(game.hypes),
            	popularity=float(game.popularity),
            	critics_rating=float(game.critics_rating),
            	# genres
            	positive_reviews_steam=int(game.positive_reviews_steam),
            	negative_reviews_steam=int(game.negative_reviews_steam),
            	owners=int(game.owners),
            	average_forever=int(game.average_forever),
            	average_2weeks=int(game.average_2weeks),
            	price=int(game.price),
            	# language
            	count_videos=int(game.count_videos),
            	count_views=int(game.count_views),
            	count_likes=int(game.count_likes),
            	count_dislikes=int(game.count_dislikes),
            	count_comments=int(game.count_comments),
            	# view_count
            	# follows
            	# language
            	# started_at
            	# type
            	# viewer_count
            )
            new_game.save()
            count+=1
