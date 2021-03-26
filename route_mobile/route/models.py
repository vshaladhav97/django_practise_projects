from django.db import models

# Create your models here.


class Items(models.Model):
    id = models.AutoField()
    status = models.CharField(max_length=20)
    item = models.CharField(max_length=20)