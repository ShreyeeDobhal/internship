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
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':('Phone')}),label=("Phone number"), required=True)
    valid_till=forms.DateField(label=('Enter the last date of applying in yy-mm-dd format'),widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Date'}))
    requirements=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Requirements'}))
    hear=forms.ChoiceField(label=('Where did you hear of us?'), choices=(('Mail',"Mail"),('Tv',"Tv"),('Newspapaer',"Newspapaer"),('other',"other")))
    jobType=forms.ChoiceField(label=('What Type of Employment is it?'), 
                               choices=(('Full time',"Full time"),('Part time',"Part time")))
    
    country = CountryField().formfield()
    
    
    
    
    class Meta:
        model=Jobpost
        fields = ('JobTitle','JobDesciption','Jobindustry',
        'CompanyName','company_logo','location','requirements',
        'email' ,
        'phone_number','valid_till', 
        
        'jobType','hear','contractType','country',)
               