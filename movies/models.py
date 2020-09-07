from django.db import models
from core.models import AbstractItem


class Movie(AbstractItem):
    cover_image = models.ImageField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="movies"
    )
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="movies"
    )
    cast = models.ManyToManyField("people.Person")

    def __str__(self):
        return self.title

