from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import redirect, reverse
from movies.models import Movie


class MovieListView(ListView):
    model = Movie
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "movies"

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(MovieListView, self).dispatch(request, *args, **kwargs)

        except Http404:
            return redirect(reverse("core:home"))