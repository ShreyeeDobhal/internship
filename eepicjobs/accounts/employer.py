from django import forms
from .models import Employer
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class EmployerForm(forms.ModelForm):
    widgets = {
            'Established_date': forms.DateInput(attrs={'class':'datepicker'})}
    class Meta:
        model=Employer
        fields = '__all__'