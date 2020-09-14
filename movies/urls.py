from django.urls import path
from movies.views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView

app_name = "movies"

urlpatterns = [
    path("", MovieListView.as_view(), name="movies"),
    path("create", MovieCreateView.as_view(), name="movie_create"),
    path("update/<int:pk>", MovieUpdateView.as_view(), name="movie_update"),
    path("<int:pk>", MovieDetailView.as_view(), name="movie_detail"),
]
