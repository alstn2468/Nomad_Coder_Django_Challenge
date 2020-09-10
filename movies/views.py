from django.shortcuts import render


def resolve_movies(request):
    return render(request, "movies/movie_list.html")
