from django.urls import include, path
from .views import *

urlpatterns = [
    path('', GamesView.as_view(), name="games_view"),
    path('get_data/<str:graphtype>/<str:yaxis>/<str:xaxis>/', GetGraphicData.as_view(), name="get_data"),
    path('get_data/<str:graphtype>/<str:yaxis>/<str:xaxis>/<str:name>', GetGraphicData.as_view(), name="get_game_data"),
    path('get_data/table/<str:table_type>', GetTableData.as_view(), name="get_table_data"),
    path('colors/', GenreColors.as_view(), name="genre_colors"),
    path('genres/', Genres.as_view(), name="genres")
]
