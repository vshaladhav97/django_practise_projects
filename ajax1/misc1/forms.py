# from .models import user
from django import forms
from .models import User


# class SignupForm(forms.ModelForm):
#     password = forms.CharField(Max_length=100, label="password")
#     password1 = forms.CharField(max_length=100, lable="confirmPassword")

#     def __init__(self, data=None):
#         super().__init__(data=data)
#         self.fields['name'].widget.attrs['class'] = 'form-control'
#         self.fields['password'].widget = forms.PasswordInput()
#         self.fields['password1'].widget = forms.PasswordInput()
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'

#     class Meta:
#         model = User
#         fields = "__all__"

#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if ' ' not in name:
#             raise ValidationError('Both First and Last Name required')
#         return name




class JoinForm(forms.Form): 
    email = forms.EmailField()
    name = forms.CharField(max_length=120)