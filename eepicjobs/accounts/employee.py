from django import forms
from .models import Employee
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class EmployeeForm(forms.ModelForm):
   
    class Meta:
        model=Employee
        fields = '__all__'