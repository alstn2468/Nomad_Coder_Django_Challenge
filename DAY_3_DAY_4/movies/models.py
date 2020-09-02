from django.db import models
from core.models import AbstractItem

"""
Here are the models you have to create:
- Movie:
  title
  year
  cover_image
  rating
  category (ManyToMany => categories.Category)
  director (ForeignKey => people.Person)
  cast (ManyToMany => people.Person)
"""


class Movie(AbstractItem):
    cover_image = models.ImageField(upload_to="movie_images", blank=True)
    category = models.ForeignKey(
        "categories.Category", related_name="movie_category", on_delete=models.CASCADE
    )
    director = models.ForeignKey(
        "people.Person", related_name="movie_director", on_delete=models.CASCADE
    )
    cast = models.ForeignKey(
        "people.Person", related_name="movie_cast", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Movie"
