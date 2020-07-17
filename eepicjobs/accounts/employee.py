from django import forms
from .models import Employee
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class EmployeeForm(forms.ModelForm):
   
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