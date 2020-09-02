from django.db import models
from django.contrib.auth.models import AbstractUser
from categories.models import Category


def set_cateogry_fk_model():
    return Category.objects.all()[:1].get()


class User(AbstractUser):

    PREF_BOOKS = "books"
    PREF_MOVIES = "movies"
    PREF_CHOICES = ((PREF_BOOKS, "Books"), (PREF_MOVIES, "Movies"))

    LANG_EN = "english"
    LANG_KR = "korean"
    LANG_CHOICES = ((LANG_EN, "English"), (LANG_KR, "Korean"))

    bio = models.TextField()
    preference = models.CharField(
        max_length=20, choices=PREF_CHOICES, default=PREF_MOVIES
    )
    language = models.CharField(max_length=20, choices=LANG_CHOICES, default=LANG_EN)
    fav_book_genre = models.ForeignKey(
        "categories.Category",
        related_name="fav_book_genre",
        on_delete=models.SET(set_cateogry_fk_model),
    )
    fav_movie_genre = models.ForeignKey(
        "categories.Category",
        related_name="fav_movie_genre",
        on_delete=models.SET(set_cateogry_fk_model),
    )

