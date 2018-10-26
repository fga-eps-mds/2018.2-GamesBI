from django.urls import include, path
from .views import GamesView
urlpatterns = [
    path('/', GamesView.as_view(), name="games_view"),
    path('games', GamesView.as_view())
]
