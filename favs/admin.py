from django.contrib import admin
from favs.models import FavList


@admin.register(FavList)
class FavListAdmin(admin.ModelAdmin):
    list_display = (
        "created_by",
        "get_books",
        "get_movies",
    )

    list_filter = (
        "created_by__username",
        "books__title",
        "movies__title",
    )

    def get_books(self, obj):
        return ",".join([str(book) for book in obj.books.all()])

    def get_movies(self, obj):
        return ",".join([str(movie) for movie in obj.movies.all()])
