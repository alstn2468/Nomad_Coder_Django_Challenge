from django.urls import path
from movies.views import movie_list

app_name = "movies"

urlpatterns = [
    path("", movie_list, name="movie_list"),
]