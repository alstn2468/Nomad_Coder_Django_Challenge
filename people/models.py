from django.db import models
from core.models import AbstractTimeStamp

"""
- Person
  name
  kind (choice=Actor/Director/Writer)
  photo
"""


class Person(AbstractTimeStamp):
    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "Writer"
    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=8, choices=KIND_CHOICES, default=KIND_ACTOR)
    photo = models.ImageField(upload_to="person_images")

    def __str__(self):
        return self.name
