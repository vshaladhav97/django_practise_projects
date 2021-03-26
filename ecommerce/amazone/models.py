from django.db import models
from csvs.models import Csv
# Create your models here.
class Product(models.Model):
    
    # id = models.AutoField(primary_key=True)
    ids = models.ForeignKey(Csv, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    manufacturer = models.CharField(max_length=300,
                                    blank=True)
    price = models.IntegerField
    status = models.SmallIntegerField()
    
    def __str__(self):
        return self.name