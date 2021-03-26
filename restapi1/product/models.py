from django.db import models

# Create your models here.
class Products(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.name