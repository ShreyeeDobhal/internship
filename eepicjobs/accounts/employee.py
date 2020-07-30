from django import forms
from .models import Employee
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class EmployeeForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    #phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':('Phone')}),label=("Phone number"), required=True)
    #valid_till=forms.DateField(label=('Enter the last date of applying in yy-mm-dd format'),widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Date'}))
    experience_tenure=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Experience tenure in years'}))
    # projects=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Projects'}))
    linked_in=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))   
    insta=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))     
    twitter=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))    
    Website=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))    
    about_yourself=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'About You'}))
    youtube_url=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))    
    about_yourself=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Aout You'}))
    profession=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'profession'}))
    salary_amount=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Salary Amount'}))
    location=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}))
    Facebook=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))    

    class Meta:
        model=Employee
        fields =['profile_photo',"name", 
   'profession',
   
    "gender",
    "experience_tenure",
   
    "experience_level",
    
    "qualification",
    "contract_type",
    "phone_number",
   
    
   "salry_type",
    "salary_amount",
    "salary_currency",
   "Marital_status",
    "set_your_profile",
    "about_yourself",
    "email",
    "company_specialization",
    "location",
    "Facebook"]