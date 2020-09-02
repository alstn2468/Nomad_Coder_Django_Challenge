from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "created_by",
        "text",
        "rating",
        "movie",
        "book",
    )

    list_filter = (
        "created_by__username",
        "movie",
        "book",
    )

