from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import escape
# Create your models here.


class AmazoneCustomer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # lastname = models.CharField(max_length=200)
    # email = models.EmailField(blank=True)
    description = models.CharField(max_length=200)
    # birth_date = models.DateField()

    price = models.IntegerField()
    availablity = models.BooleanField(default=False)
    available = models.IntegerField(default=0)
    images = models.ImageField(upload_to='images')
    # status = models.SmallIntegerField(blank=False)
    # contact = models.CharField(max_length=100, blank=True)
    # <img src="{}", width="100"/>

    def admin_photo(self):
        return mark_safe('<img src="{}", width="100"/>'.format(self.images.url))
    
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
    

    # def __str__(self):
    #     return self.id.__str__()


class Amazone(models.Model):
    amazonecustomer = models.ForeignKey(
        AmazoneCustomer, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.amazonecustomer
