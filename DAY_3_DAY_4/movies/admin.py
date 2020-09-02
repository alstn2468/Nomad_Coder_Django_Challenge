from django.contrib import admin
from movies.models import Movie
from django.contrib.admin.filters import AllValuesFieldListFilter


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "year",
        "category",
        "rating",
        "director",
        "created_at",
        "updated_at",
    )

    list_filter = (
        ("year", AllValuesFieldListFilter),
        "category__name",
        "director__name",
        "cast__name",
    )
