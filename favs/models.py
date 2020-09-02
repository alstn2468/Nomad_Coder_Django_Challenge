from django.db import models
from core.models import AbstractTimeStamp

"""
Here are the models you have to create:
- FavList
  created_by (OneToOne => users.User)
  books (ManyToMany => books.Book)
  movies (ManyToMany => movies.Movie)
"""


class FavList(AbstractTimeStamp):
    created_by = models.OneToOneField("users.User", on_delete=models.CASCADE)
    books = models.ManyToManyField("books.Book")
    movies = models.ManyToManyField("movies.Movie")
