from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    PREFERENCE_BOOKS = "books"
    PREFERENCE_MOVIES = "movies"

    PREFERENCE_CHOICES = (
        (PREFERENCE_BOOKS, "Books"),
        (PREFERENCE_MOVIES, "Movies"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"),
                        (LANGUAGE_KOREAN, "Korean"))

    bio = models.TextField(blank=True)
    preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=6, blank=True, default=PREFERENCE_BOOKS
    )
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_KOREAN
    )
    favourite_book_genre = models.TextField(blank=True)
    favourite_movie_genre = models.TextField(blank=True)
