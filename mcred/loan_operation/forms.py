# from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    """sign up form fields"""
    class Meta:
        model = User
        fields = ['username','email', 'dob', 'mobile_no', 'pan_no', 'address', 'city', 'state' ]