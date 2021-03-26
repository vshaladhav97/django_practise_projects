from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.name
