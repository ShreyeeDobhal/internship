from django import forms
from .models import Jobexperience
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class JobexperienceForm(forms.ModelForm):
    Organization_name1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False,label="Enter Organization name")
    your_role1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False,label="Enter Your position in above mentioned organization")
    jobtenure1=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Time period of above job'}),required=False,label="Enter your tenure for the above job in years")
    Organization_name2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False,label="Enter Organization name")
    your_role2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False,label="Enter Your position in above mentioned organization")
    jobtenure2=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Time period of above job'}),required=False,label="Enter your tenure for the above job in years")
    Organization_name3=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False,label="Enter Organization name")
    your_role3=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False,label="Enter Your position in above mentioned organization")
    jobtenure3=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Time period of above job'}),required=False,label="Enter your tenure for the above job in years")
    Organization_name4=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False,label="Enter Organization name")
    your_role4=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False,label="Enter Your position in above mentioned organization")
    jobtenure4=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Time period of above job'}),required=False,label="Enter your tenure for the above job in years")
    Organization_name5=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False,label="Enter Organization name")
    your_role5=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False,label="Enter Your position in above mentioned organization")
    jobtenure5=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Time period of above job'}),required=False,label="Enter your tenure for the above job in years")
    Organization_name6=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False,label="Enter Organization name")
    your_role6=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False,label="Enter Your position in above mentioned organization")
    jobtenure6=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Time period of above job'}),required=False,label="Enter your tenure for the above job in years")
    
    
    class Meta:
        model=Jobexperience
        fields = ["Organization_name1","your_role1","jobtenure1","Organization_name2","your_role2","jobtenure2","Organization_name3","your_role3","jobtenure3","Organization_name4","your_role4","jobtenure4","Organization_name5","your_role5","jobtenure5","Organization_name6","your_role6","jobtenure6"]