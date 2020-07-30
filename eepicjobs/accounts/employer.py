from django import forms
from .models import Employer
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class EmployerForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    #phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':('Phone')}),label=("Phone number"), required=True)
    #valid_till=forms.DateField(label=('Enter the last date of applying in yy-mm-dd format'),widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Date'}))
    no_of_employees=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Preveious mployments'}))
    # projects=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Projects'}))
    linked_in=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))   
    insta=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))     
    twitter=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))    
    Website=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))    
    about_yourself=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'About You'}))
    youtube_url=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))    
    about_yourself=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Aout You'}))
    location=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}))
    Facebook=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))    
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