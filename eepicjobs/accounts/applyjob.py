from django import forms
from .models import applicant
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES

class applicantform(forms.ModelForm):

    class Meta:
            model=applicant
            fields = ('name',
        'email' ,
        'phone_number','education_details',
        'prev_Employments','skills','projects','accomplishments','experience','otherLinks')