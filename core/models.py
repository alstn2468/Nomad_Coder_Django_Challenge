from django.db import models
from datetime import datetime


class AbstractTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractItem(AbstractTimeStamp):
    title = models.CharField(max_length=120)
    year = models.PositiveIntegerField(default=datetime.now().year)
    rating = models.FloatField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
