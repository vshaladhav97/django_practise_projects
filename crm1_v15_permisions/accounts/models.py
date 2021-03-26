from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name



	
class User(AbstractUser):
    
    # Define the extra fields
    # related to User here
    first_name = models.CharField(_('First Name of User'), blank=True, max_length=20)
    last_name = models.CharField(_('Last Name of User'), blank=True, max_length=20)

# More User fields according to need

    # define the custom permissions
    # related to User.
    class Meta:

        permissions = (
            ("can_view_employees", "Can See Employees"),
            ("can_edit_in_Employees", "Can Edit Employees"),
            ("can_delete_in_Employees", "Can Delete Employees"),
            ("can_view_addressdetails", "Can See Employees"),
            ("can_edit_in_addressdetails", "Can Edit addressdetails"),
            ("can_delete_in_addressdetails", "Can Delete addressdetails"))
