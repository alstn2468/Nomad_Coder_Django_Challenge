from django.urls import reverse
from django.db import models
from core.models import AbstractItem


class Movie(AbstractItem):
    cover_image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="movies"
    )
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="movies"
    )
    cast = models.ManyToManyField("people.Person")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"pk": self.pk})
