from django.urls import include, path
from .views import *
urlpatterns = [
    path('', GamesView.as_view(), name="games_view"),
    path('get_data/<str:graphtype>/<str:yaxys>/<str:xaxys>/', GetGraphicData.as_view(), name="steam_data"),
    path('search_game', SearchGame.as_view(), name="search_game"),
]
