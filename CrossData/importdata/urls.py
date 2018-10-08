from django.urls import include, path
from .views import GamesView

urlpatterns = [
    path('get_games_list/', GamesView.as_view(), name="get_games")
]
