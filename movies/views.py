from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.http import Http404
from django.shortcuts import redirect, reverse
from movies.models import Movie


class MovieListView(ListView):
    model = Movie
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Movies"
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(MovieListView, self).dispatch(request, *args, **kwargs)

        except Http404:
            return redirect(reverse("core:home"))


class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = kwargs["object"]
        context["page_title"] = movie.title

        return context


class MovieCreateView(CreateView):
    model = Movie
    fields = [
        "title",
        "year",
        "cover_image",
        "category",
        "director",
        "cast",
        "rating",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Movie"

        return context


class MovieUpdateView(UpdateView):
    model = Movie
    fields = [
        "title",
        "year",
        "cover_image",
        "category",
        "director",
        "cast",
        "rating",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Movie"

        return context