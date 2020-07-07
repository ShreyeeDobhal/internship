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
    #phone
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    country = CountryField().formfield()
    jobType=forms.ChoiceField(label=('What Type of Job are you Looking for?'), 
                               choices=(('0',"Full time"),('1',"Part time")))
    hear=forms.ChoiceField(label=('Where did you hear of us?'), choices=(('0',"Mail"),('1',"Tv"),('2',"Newspapaer"),('3',"other")))
    class Meta:
        model=Jobpost
        fields = ('JobTitle','JobDesciption',
        'CompanyName',
        'email' ,
        'phone_number', 
        'country',
        'jobType','hear','contractType')
               