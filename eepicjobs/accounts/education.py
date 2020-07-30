from django import forms
from .models import Education
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class EducationForm(forms.ModelForm):
    masters_degree=forms.CharField(label='Mention Your Master Degree if any(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Master's details"}),required=False)
    CGPA_For_masters=forms.FloatField(label='Mention your cgpa in masters(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Master's details"}),required=False)
    yop_for_masters=forms.IntegerField(label='Mention year of passing  for masters(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Master's details"}),required=False)
    school=forms.CharField(label='Mention Your Master Degree if any(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"school"}))
    
    college=forms.CharField(label='Mention Your Master Degree if any(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"college"}))
    tenth_percentage=forms.FloatField(label='Mention your cgpa in masters(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"10 %"}))
    twelth_percentage=forms.FloatField(label='Mention your cgpa in masters(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"12 %"}))
    yop_for_tenth=forms.IntegerField(label='Mention year of passing  for masters(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"yop_for_tenth"}))
    yop_for_twelfth=forms.IntegerField(label='Mention year of passing  for masters(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"yop_for_twelfth"}))
    bachelor_degree=forms.CharField(label='Mention Your Master Degree if any(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Bachelor degree"}))
    CGPA_For_bachelors=forms.FloatField(label='Mention your cgpa in masters(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"CGPA"}))

    yop_for_bachelors=forms.IntegerField(label='Mention year of passing  for masters(optional)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"yop_for_bachelors"}))
    class Meta:
        model=Education


        fields = ["school",
        "college","tenth_percentage","yop_for_tenth","twelth_percentage","yop_for_twelfth","bachelor_degree","yop_for_bachelors","CGPA_For_bachelors","masters_degree","yop_for_masters","CGPA_For_masters"
        ]