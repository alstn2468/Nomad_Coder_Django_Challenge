from django.db import models
from core.models import AbstractTimeStamp

"""
Here are the models you have to create:
- Review
  created_by (ForeignKey => users.User)
  text
  movie (ForeignKey => movies.Movie, null,blank)
  book (ForeignKey => movies.Movie, null,blank)
  rating
"""


class Review(AbstractTimeStamp):
    created_by = models.ForeignKey(
        "users.User", related_name="user", on_delete=models.CASCADE
    )
    text = models.TextField()
    rating = models.FloatField(default=0)
    movie = models.ForeignKey(
        "movies.Movie",
        related_name="movie",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    book = models.ForeignKey(
        "books.Book",
        related_name="book",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

