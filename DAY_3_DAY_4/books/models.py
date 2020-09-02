from django.db import models
from core.models import AbstractItem

"""
Here are the models you have to create:
- Book:
  title
  year
  category (ForeignKey => categories.Category)
  cover_image
  rating
  writer (ForeignKey => people.Person)
"""


class Book(AbstractItem):
    cover_image = models.ImageField(upload_to="book_images", null=True)
    category = models.ForeignKey(
        "categories.Category", related_name="book_category", on_delete=models.CASCADE
    )
    writer = models.ForeignKey(
        "people.Person", related_name="book_writer", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Book"
