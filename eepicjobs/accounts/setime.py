from django import forms
from .models import settime
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class settimeForm(forms.ModelForm):
    widgets = {
            'indate': forms.DateInput(attrs={'class':'datepicker'})}
    widgets = {
            'intime': forms.DateInput(attrs={'class':'timepicker'})}    
    class Meta:
        model=settime
        fields = ['indate','intime']