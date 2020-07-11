from django import forms
from .models import subscriptionpack
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
class subscriptionpackForm(forms.ModelForm):
    widgets = {
            'purchsedate': forms.DateInput(attrs={'class':'datepicker'})}
    class Meta:
        model=subscriptionpack
        fields = '__all__'