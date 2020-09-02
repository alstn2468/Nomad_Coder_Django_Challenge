from django.db import models
from datetime import datetime


class AbstractTimeStamp(models.Model):
    """Abstract TimeStamp Model
    Inherit:
        Model
    Fields:
        created_at : DateTimeField (UnEditable)
        updated_at : DateTimeField (Editable)
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractItem(AbstractTimeStamp):
    YEAR_CHOICES = []

    for r in range(1980, (datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    title = models.CharField(max_length=60)
    year = models.PositiveIntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    rating = models.FloatField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
