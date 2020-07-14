from django import forms
from .models import Jobexperience
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class JobexperienceForm(forms.ModelForm):
    
    class Meta:
        model=Jobexperience
        fields = '__all__'