from django import forms
from .models import Jobpost
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES

class JobPostform(forms.ModelForm):
    JobTitle=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Job Title'}))
    JobDesciption=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Job Description'}))
    CompanyName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Comapany Name'}))
    Jobindustry=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Jobindustry'}))
    location=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    country = CountryField().formfield()
    jobType=forms.ChoiceField(label=('What Type of Job are you Looking for?'), 
                               choices=(('Full time',"Full time"),('Part time',"Part time")))
    hear=forms.ChoiceField(label=('Where did you hear of us?'), choices=(('Mail',"Mail"),('Tv',"Tv"),('Newspapaer',"Newspapaer"),('other',"other")))
    class Meta:
        model=Jobpost
        fields = ('JobTitle','JobDesciption','Jobindustry',
        'CompanyName','company_logo','location',
        'email' ,
        'phone_number','valid_till', 
        'country',
        'jobType','hear','contractType','requirements',)
               