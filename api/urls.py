from django.urls import path, include
from .views import get_games, get_genres

urlpatterns = [
    path("games", get_games),
    path("genres", get_genres)
]