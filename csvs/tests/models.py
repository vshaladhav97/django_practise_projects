from django.db import models

# Create your models here.
class Csv(models.Model):
    # id = models.ForeignKey(Csv, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    file_name = models.FileField(upload_to='tests')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    
    def __str__(self):
        return f"File id: {self.id}"
    
class Product(models.Model):
    
    # id = models.AutoField(primary_key=True)
    ids = models.ForeignKey(Csv, on_delete=models.CASCADE)  
    name = models.CharField(max_length=300)
    description = models.TextField()
    manufacturer = models.CharField(max_length=300,
                                    blank=True)
    price = models.IntegerField()
    status = models.SmallIntegerField()
    
    def __str__(self):
        return self.name