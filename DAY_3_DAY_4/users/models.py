from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    PREF_BOOKS = "books"
    PREF_MOVIES = "movies"
    PREF_CHOICES = ((PREF_BOOKS, "Books"), (PREF_MOVIES, "Movies"))

    LANG_EN = "english"
    LANG_KR = "korean"
    LANG_CHOICES = ((LANG_EN, "English"), (LANG_KR, "Korean"))

    GENRE_ACTION = "action"
    GENRE_COMEDY = "comedy"
    GENRE_THRILLER = "thriller"
    GENRE_HISTORY = "history"

    GENRE_CHOICES = (
        (GENRE_ACTION, "Action"),
        (GENRE_COMEDY, "Comedy"),
        (GENRE_THRILLER, "Thriller"),
        (GENRE_HISTORY, "History"),
    )

    bio = models.TextField()
    preference = models.CharField(max_length=20, choices=PREF_CHOICES, default=PREF_MOVIES)
    language = models.CharField(max_length=20, choices=LANG_CHOICES, default=LANG_EN)
    fav_book_genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default=GENRE_HISTORY)
    fav_movie_genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default=GENRE_HISTORY)
