from django import forms
from .models import Project
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class ProjectsForm(forms.ModelForm):
    project1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project'}),required=False)
    project2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project'}),required=False)
    project3 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project'}),required=False)
    project4 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project'}),required=False)
    project5 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project'}),required=False)
    project6 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project'}),required=False)
    project7 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project'}),required=False)
    project8 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project'}),required=False)
    project9 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project'}),required=False)
    project10 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project'}),required=False)
    class Meta:
        model=Project
        fields = ['project1','project2','project3','project4','project5','project6','project9','project7','project8','project10']