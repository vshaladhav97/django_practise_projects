from django.db import models
from django.utils.text import slugify 
import string 
import random

# Create your models here.
def code_generator(size = 6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



class BookStore(models.Model):
    BOOK_CHOICES = (
        ('Science', 'Science'),
        ('Maths', 'Maths'),
        ('Geometry', 'Geometry'),
        ('English', 'English'),
        ('History', 'History'),    
    )
    
    
    title = models.CharField(max_length=100, choices=BOOK_CHOICES)
    name = models.CharField(max_length=70)
    shortcut = models.CharField(max_length=15, unique=True) 


    def save(self, *args, **kwargs): 
        self.shortcut = code_generator()
        super(BookStore, self).save(*args, **kwargs) 

    
    def __str__(self):
        return self.name
    