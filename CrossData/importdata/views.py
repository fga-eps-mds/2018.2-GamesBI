import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# from .serializers import GameSerializer

import pandas as pd

class GamesView(APIView):

    @api_view(('GET',))
    def search_game(request, nome):
        data = {'name': nome}
        queryset = Game.objects.filter(name=nome)
        serializer = self.get_serializer(queryset,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
