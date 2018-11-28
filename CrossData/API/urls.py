from django.urls import include, path
from .genre_data import *
from .table_data import *
from .graphic_data import *
from .games_view import *

urlpatterns = [
    path('', GetGamesView.as_view(), name="games_view"),
    path('get_data/<str:graphtype>/<str:yaxis>/<str:xaxis>/', GetGraphicData.as_view(), name="get_data"),
    path('get_data/<str:graphtype>/<str:yaxis>/<str:xaxis>/<str:name>', GetGraphicData.as_view(), name="get_game_data"),
    path('get_data/table/<str:table_type>', GetTableData.as_view(), name="get_table_data"),
    path('colors/', GetGenreColors.as_view(), name="genre_colors"),
    path('genres/', GetGenres.as_view(), name="genres")
]
