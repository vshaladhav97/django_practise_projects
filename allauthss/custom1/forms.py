from allauth.account.forms import SignupForm
from django import forms


class CoreSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    phone_number = forms.CharField(max_length=50, label='Phone Number')

    def custom_signup(self, request, user):
        # print(self.cleaned_data, user)
        user.first_name = self.cleaned_data['first_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        # print(user)
        return user