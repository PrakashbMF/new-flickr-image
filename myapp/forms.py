from django import forms
from django.contrib.auth.models import User

from myapp.models import ExtendedUser


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'firstnameid'}) ,
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'lastnameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'})
        }


class ExtendedUserForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['phone', 'age']
        widgets = {
            'phone': forms.NumberInput(attrs={'class': ' form-control', 'id': 'phoneid'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'id': 'ageid'})
        }
