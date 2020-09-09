from django.urls import path
from core.views import search, genre, home

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("genre/", genre, name="genre"),
    path("search/", search, name="search"),
]