import requests

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from CrossData.API.models import *
from CrossData.API.serializers import *
from .objects_attrs import *


class GetGraphicData(APIView):

    '''
            Endpoint to return data
            to be used in graphics
    '''

    def get(self, request, graphtype, yaxis, xaxis, name=None, format=None):

        graph_type = graphtype
        data = {}
        y_axis = yaxis
        x_axis = xaxis

        if name is None:
            if graph_type == "line":
                data = self.get_line_axis(y_axis, x_axis, data)

        else:
            game = self.get_game(name)
            data['x_axis'] = self.get_dates(game)
            data['y_axis'] = self.get_game_y_axis(game, y_axis)

        return Response(data=data, status=status.HTTP_200_OK)

    def get_game_y_axis(self, game, y_axis):

        y_axis_data = []
        infos = []

        if y_axis in steam_attrs:
            infos = InfoSteam.objects.all().filter(game=game)
        elif y_axis in youtube_attrs:
            infos = InfoYoutube.objects.all().filter(game=game)
        elif y_axis in twitch_attrs:
            infos = InfoTwitch.objects.all().filter(game=game)
        elif y_axis in streams_attrs:
            infos = TwitchStream.objects.all().filter(game=game)

        y_axis_data = self.get_data(infos, y_axis)

        return y_axis_data

    def get_dates(self, game):
        dates = []
        infos = InfoSteam.objects.filter(game=game)
        for info in infos:
            date = (
                str(info.date.date().year)+"/" +
                str(info.date.date().month)+"/"+str(info.date.date().day)
            )
            dates.append(date)

        return dates

    def get_game(self, game_name):

        game = Game.objects.get(name=game_name)
        return game

    def get_line_axis(self, y_axis, x_axis, game_data):
        if x_axis == 'games' or y_axis == 'games':
            game_data['x_axis'] = self.get_games_name()

        ordered = order(InfoSteam.objects, [
                        'owners', 'positive_reviews_steam',
                        'average_2weeks'], 20)

        if y_axis in steam_attrs:
            game_data['y_axis'] = self.get_data(
                ordered,
                y_axis
            )
        if x_axis in steam_attrs:
            game_data['x_axis'] = self.get_data(
                ordered,
                x_axis
            )

        if y_axis in youtube_attrs:
            game_data['y_axis'] = self.get_data(
                ordered,
                y_axis
            )

        if x_axis in youtube_attrs:
            game_data['x_axis'] = self.get_data(
                ordered,
                x_axis
            )

        if y_axis in twitch_attrs:
            game_data['y_axis'] = self.get_data(
                ordered,
                y_axis
            )
        if x_axis in twitch_attrs:
            game_data['x_axis'] = self.get_data(
                ordered,
                x_axis
            )

        return game_data

    def get_data(self, db_data, attr):

        collected_data = []

        for data in db_data:

            try:
                new_data = getattr(data, attr)
                collected_data.append(new_data)
            except AttributeError:
                pass

        return collected_data

    def get_games_name(self):
        game_names = []
        for game in order(InfoSteam.objects, ['owners',
                                              'positive_reviews_steam',
                                              'average_2weeks'], 20):
            game_names.append(game.game.name)

        return game_names

def order(query_set, attrs, quantity, reverse=True):
    all_games = Game.objects.all()

    updated_infos = []
    for game in all_games:
        if(len(query_set.filter(game=game)) != 0):
            updated_infos.append(query_set.filter(game=game).latest('date'))

    games = sorted(updated_infos, key=lambda x: [getattr(
        x, y) for y in attrs], reverse=reverse)[:quantity]
    return games
