from django import forms
from .models import Education
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields = '__all__'