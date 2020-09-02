from django.contrib import admin
from books.models import Book
from django.contrib.admin.filters import AllValuesFieldListFilter


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "year",
        "category",
        "rating",
        "writer",
        "created_at",
        "updated_at",
    )

    list_filter = (
        ("year", AllValuesFieldListFilter),
        "category__name",
        "writer__name",
    )
