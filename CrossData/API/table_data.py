import requests

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from CrossData.API.models import *
from CrossData.API.serializers import *
import datetime


class GetTableData(APIView):

    '''
            Endpoint to return data
            to be used in tables
    '''

    def get(self, request, table_type, format=None):

        collected_data = []

        if table_type == "trendingnow":
            collected_data = self.get_tranding_now_data()

        elif table_type == "mostwatched":
            collected_data = self.get_most_watched_data()

        elif table_type == "sales":
            collected_data = self.get_sales_data()

        elif table_type == "playedtime":
            collected_data = self.get_by_playedtime()

        if len(collected_data) != 0:
            status_code = status.HTTP_200_OK
        else:
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(data=collected_data, status=status_code)

    def get_by_playedtime(self):
        infos = order(InfoSteam.objects, [
                      'average_2weeks', 'average_forever',
                      'positive_reviews_steam'], 20)
        games = [x.game for x in infos]

        return self.get_data(games)

    def get_sales_data(self):
        infos = order(InfoSteam.objects.exclude(price=0),
                      ['owners', 'average_2weeks'], 20)
        games = [x.game for x in infos]

        return self.get_data(games)

    def get_tranding_now_data(self):
        if Game.objects.all().count() == 0:
            return []

        recent_games = list(Game.objects.order_by('-release_date')[:25])
        date = recent_games[-1].release_date

        infos = order(InfoSteam.objects.filter(game__release_date__range=[
                      date, datetime.datetime.now()]),
                      ['positive_reviews_steam', 'average_2weeks'], 20)

        games = [x.game for x in infos]

        return self.get_data(games)

    def get_most_watched_data(self):

        attrs = ['count_views', 'count_videos', 'count_comments']

        infos = order(InfoYoutube.objects, attrs, 20)
        games = [x.game for x in infos]

        return self.get_data(games)

    def get_data(self, games):

        collected_data = []

        for game in games:

            game_data = {}

            info_steam = InfoSteam.objects.filter(game=game).latest('date')
            info_youtube = InfoYoutube.objects.filter(game=game).latest('date')
            info_twitch = InfoTwitch.objects.filter(game=game).latest('date')

            game_data['game'] = game.name
            game_data['owners'] = info_steam.owners
            game_data['price'] = info_steam.price
            game_data['positive_reviews_steam'] = info_steam.positive_reviews_steam
            game_data['youtube_views'] = info_youtube.count_views
            game_data['youtube_count_likes'] = info_youtube.count_likes
            game_data['youtube_count_dislikes'] = info_youtube.count_dislikes
            game_data['twitch_viewer_count'] = info_twitch.viewer_count

            collected_data.append(game_data)

        return collected_data

def order(query_set, attrs, quantity, reverse=True):
    all_games = Game.objects.all()

    updated_infos = []
    for game in all_games:
        if(len(query_set.filter(game=game)) != 0):
            updated_infos.append(query_set.filter(game=game).latest('date'))

    games = sorted(updated_infos, key=lambda x: [getattr(
        x, y) for y in attrs], reverse=reverse)[:quantity]
    return games
