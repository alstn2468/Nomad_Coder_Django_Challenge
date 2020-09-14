from django.urls import path
from movies.views import MovieListView, MovieDetailView

app_name = "movies"

urlpatterns = [
    path("", MovieListView.as_view(), name="movies"),
    path("<int:pk>", MovieDetailView.as_view(), name="movie_detail"),
]
