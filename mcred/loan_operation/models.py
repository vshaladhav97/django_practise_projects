from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    """extended user model"""

    dob = models.DateField(blank=True, null=True)
    mobile_no = models.CharField(max_length=10)
    pan_no = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)


class Loan(models.Model):
    """loan table """
    user_id = models.ForeignKey(
        User, related_name="users", on_delete=models.CASCADE)

    loan_amount = models.IntegerField()
    loan_duration = models.IntegerField()
    rate_of_interest = models.DecimalField(max_digits=5, decimal_places=1)
    interest_amount = models.IntegerField()
    final_amount = models.IntegerField()
    loan_limit = models.IntegerField(default=100000)
    due_date = models.DateField(blank=True, null=True)
    transaction_date = models.DateTimeField(
        editable=False, blank=True, null=True)
    amt_paid_by_the_bank = models.IntegerField() 
    user_has_to_pay = models.IntegerField()
    

    def save(self, *args, **kwargs):
        self.transaction_date = timezone.now()
        return super(Loan, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.interest_amount)
