from django.db import models

# Create your models here.

class Data(models.Model):
    place = models.ForeignKey(Places)
    time = models.DateTimeField()
    data_1 = models.DecimalField(max_digits=3, decimal_places=1)
    data_2 = models.DecimalField(max_digits=3, decimal_places=1)
    data_3 = models.DecimalField(max_digits=4, decimal_places=1)