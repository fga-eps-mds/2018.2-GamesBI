import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from CrossData.API.models import *
from CrossData.API.serializers import *
from operator import itemgetter

class GetGenreColors(APIView):
    def get(self, request, format=None):
        genre_name = request.GET.get('genre')
        color_name = request.GET.get('color')

        genre = Genre.objects.get(genre=genre_name)

        colors_array = []
        for game in Game.objects.filter(genres=genre):
            colors_array.append(
                [game.r_average, game.g_average, game.b_average])

        index = ['r', 'g', 'b'].index(color_name)
        data = {"colors": sorted(colors_array, key=itemgetter(index))}
        return Response(data)


class GetGenres(APIView):
    def get(self, request, format=None):
        return Response(GenreSerializer(Genre.objects.all(), many=True).data)
