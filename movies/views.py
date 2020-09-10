from django.core.paginator import Paginator
from django.shortcuts import render
from movies.models import Movie


def resolve_movies(request):
    movies = Movie.objects.all().order_by("-created_at")
    paginator = Paginator(movies, 3)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "movies/movie_list.html",
        {
            "movies": page_obj,
        },
    )
