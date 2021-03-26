from django.db import models
from csvs.models import Csv

# Create your models here.
class Csv(models.Model):
    # id = models.ForeignKey(Csv, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    
    def __str__(self):
        return f"File id: {self.id}"