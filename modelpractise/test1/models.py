from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import ast
from jsonfield import JSONField
# from django.db import datetime
# Create your models here.

class Students(models.Model):
    stuid = models.IntegerField()
    # slug = models.SlugField(unique=True)
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=70)
    teacher = models.CharField(max_length=40, default='not avaialable')

    def __str__(self):
        return self.stuname
        # return str(self.stuid)


class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname


# Abstract Model

class BaseItem(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    title1 = models.CharField(max_length=255)
    dob = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        abstract = True
        ordering = ['title']

    def __str__(self):
        return self.title


class ItemA(BaseItem):
    content = models.TextField()

    # class Meta(BaseItem.Meta):
    #     ordering = ['-created']


class ItemB(BaseItem):
    file = models.FileField(upload_to='files')


class ItemC(BaseItem):
    file = models.FileField(upload_to='images')

# class ItemD(BaseItem):
#     slug = models.SlugField(max_length=255, unique=True)


# # Multi-table model inheritance

# class Books(models.Model):
#     title = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)

# class ISBN(Books):
#     books_ptr = models.OneToOneField(
#         Books, on_delete=models.CASCADE,
#         parent_link=True,
#         primary_key=True,
#     )
#     ISBN = models.TextField()


# # Proxy Model

# class NewManager(models.Manager):
#     pass

# class BookContent(models.Model):
#     title = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)

# class BookOrders(BookContent):
#     objects = NewManager()
#     class Meta:
#         proxy = True
#         ordering = ['created']

#     def created_on(self):
#         return timezone.now() - self.created


class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=70, unique=True)
    status = models.BooleanField()

    def __str__(self):
        return str(self.id)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

    def __str__(self):
        return str(self.id)


class Post(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    publish_date = models.DateField()
    screen = models.ImageField(upload_to='images/', null=True, blank=True)


class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    items_purchased = models.ManyToManyField(Item, through='Purchase')

    def __str__(self):
        return self.name
        


class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_purchased = models.DateField()
    quantity_purchased = models.IntegerField()
    
def validate_mails(value):
    if "@gmail.com" in value:
        return True
    else:
        raise ValidationError("This field accepts mail id of users")
    
class UserModel(models.Model):
    email = models.CharField(max_length=100, validators=[validate_mails])
    numbers = models.IntegerField(default=1,validators=[MaxValueValidator(100), MinValueValidator(1)])
    # username = models.CharField(max_length=30, null = False, validators=[RegexValidator(regex='^[a-zA-Z0-9]*$',message='Username must be Alphanumeric', code='invalid_username'),])
    
    # def __str__(self):
    #     return self.email


class MyModel(models.Model):
    myList = models.TextField(null=True)


class MyModel(models.Model): #model in which field has to be added       
    name = models.CharField(max_length=10, default='')
    json = JSONField()

    def __str__(self):
            return self.name