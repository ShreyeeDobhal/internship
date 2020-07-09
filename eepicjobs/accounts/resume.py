from django import forms
from .models import UserProfile
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class UserProfileForm(forms.ModelForm):

    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    is_emp =forms.BooleanField()
    is_seeker=forms.BooleanField()
    skills=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Skills'}))

    experience =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Experience'}))

    address =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))

    prev_Employments= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Previous employments'}))

    education_details= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Educational details'}))
    projects= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project details'}))
    accomplishments= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Accomplishments'}))
    
    class Meta:
        model=UserProfile
        fields = ('name','profile_photo',
        'email' ,'hobbies',
        'phone_number','address','education_details', 'is_emp',
        'prev_Employments','skills','projects','accomplishments','experience','otherLinks','linkedin','github','hackerrank')
        
        
        
        
        
               