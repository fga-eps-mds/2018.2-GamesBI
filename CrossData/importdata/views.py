import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from .serializers import GameSerializer

import pandas as pd

class GamesView(APIView):

    @api_view(('GET',))
    def search_game(request, name):
        data = {'nome': name}
        return Response(data, status=status.HTTP_200_OK)
