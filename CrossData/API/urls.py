from django.urls import include, path
from .views import GamesView

urlpatterns = [
    path('api/', GamesView.as_view(), name="games_view")
]
