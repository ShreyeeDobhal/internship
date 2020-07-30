from django import forms
from .models import applicant
from .models import applicantt
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

class applicanttform(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    #JobTitle=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Job Title'}))
    skills=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'skills'}))
    education_details=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'education_details'}))
    experience=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'experience'}))
    accomplishments=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'accomplishments'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    #phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':('Phone')}),label=("Phone number"), required=True)
    #valid_till=forms.DateField(label=('Enter the last date of applying in yy-mm-dd format'),widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Date'}))
    prev_Employments=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Preveious mployments'}))
    projects=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Projects'}))
    otherLinks=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL Link'}))    

    class Meta:
            model=applicantt
            fields = ('name','phone_number',
        'email' ,
        'education_details',
        'prev_Employments','skills','projects','accomplishments','experience','otherLinks')