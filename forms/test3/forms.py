from django import forms
from .models import Student
from .mixin import AjaxFormMixin
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ["name", "department", "email", "language"]
        fields = '__all__'
        

class JoinForm(AjaxFormMixin, forms.Form): # or forms.ModelForm
    email = forms.EmailField()
    name = forms.CharField(max_length=120)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == "abc@gmail.com":
            raise forms.ValidationError("This is not valid.")
        return email