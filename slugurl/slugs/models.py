from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_num = models.IntegerField(("Phone number"))

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField()
    image = models.ImageField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
