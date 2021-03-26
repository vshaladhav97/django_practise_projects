from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=25, unique=True)

class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    topic = models.ForeignKey(Topic, blank=True, null=True)