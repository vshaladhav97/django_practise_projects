from django.db import models
from django.conf import settings

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=5, null=False, primary_key=True)
    title = models.CharField(max_length=30, null=False, unique=True)
    duration = models.IntegerField(null=False)
    fee = models.IntegerField(null=False)

    def __str__(self):
        return self.code
    
    
# class Video(models.Model):
#     User= settings.AUTH_USER_MODEL
#     user= models.ForeignKey(User, null=True, on_delete= models.CASCADE)
#     name= models.CharField(max_length=500)
#     description= models.TextField()
#     videofile= models.FileField(upload_to='videos/')
    
class abc(models.Model):
    limit = models.IntegerField(default=100000)