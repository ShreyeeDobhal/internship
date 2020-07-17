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
        fields = ('name','profile_photo',
        'email' ,
        'phone_number','linked_in',"set_your_profile","about_yourself","insta",
    "twitter",
    "Website",
    "no_of_employees","Established_Date",
    "youtube_url",
    "company_specialization",
    "location",
    "Facebook")