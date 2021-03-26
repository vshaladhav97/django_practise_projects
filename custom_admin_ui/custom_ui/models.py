from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class ChessBoard(models.Model):
    board = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )