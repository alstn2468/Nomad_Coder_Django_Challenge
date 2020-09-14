from django.urls import reverse
from django.db import models
from core.models import AbstractItem


class Book(AbstractItem):
    cover_image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="books"
    )
    writer = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:book_detail", kwargs={"pk": self.pk})
