from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    user_fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "bio",
                    "preference",
                    "language",
                    "favourite_book_genre",
                    "favourite_movie_genre",
                )
            },
        ),
    )
    fieldsets = BaseUserAdmin.fieldsets + user_fieldsets

    list_filter = ("language", "preference",
                   "favourite_book_genre", "favourite_movie_genre")

    list_display = (
        "username",
        "email",
        "preference",
        "language",
        "favourite_book_genre",
        "favourite_movie_genre"
    )
