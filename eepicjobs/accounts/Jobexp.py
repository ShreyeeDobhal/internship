from django import forms
from .models import Jobexperience
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class JobexperienceForm(forms.ModelForm):
    Organization_name1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False)
    your_role1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False)
    jobtenure1=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Time period of above job'}),required=False)
    Organization_name2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False)
    your_role2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False)
    jobtenure2=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Time period of above job'}),required=False)
    Organization_name3=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False)
    your_role3=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Job Description'}),required=False)
    jobtenure3=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False)
    Organization_name4=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False)
    your_role4=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Job Description'}),required=False)
    jobtenure4=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False)
    Organization_name5=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False)
    your_role5=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Job Description'}),required=False)
    jobtenure5=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your role in the above organization'}),required=False)
    Organization_name6=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organization_name'}),required=False)
    your_role6=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Job Description'}),required=False)
    jobtenure6=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Your role in the above organization"}),required=False)
    
    
    class Meta:
        model=Jobexperience
        fields = ["Organization_name1","your_role1","jobtenure1","Organization_name2","your_role2","jobtenure2","Organization_name3","your_role3","jobtenure3","Organization_name4","your_role4","jobtenure4","Organization_name5","your_role5","jobtenure5","Organization_name6","your_role6","jobtenure6"]