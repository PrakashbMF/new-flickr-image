from django import forms
from django.contrib.auth.models import User

from myapp.models import ExtendedUser


class UserForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=20, required=True)
    # last_name = forms.CharField(max_length=20, required=True)
    # email = forms.EmailField(max_length=20, required=True)
    # username = forms.CharField(max_length=20, required=True)
    # password = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'firstnameid', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'lastnameid', 'placeholder': 'Enter Your Last Name'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'id': 'emailid', 'placeholder': 'Enter Your Email'}),
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'usernameid', 'placeholder': 'Enter Your Username'}),
            'password': forms.TextInput(
                attrs={'class': 'form-control',
                       'type': 'password', 'id': 'passwordid', 'placeholder': 'Enter Your Password'})
        }


class ExtendedUserForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['phone', 'age']
        widgets = {
            'phone': forms.NumberInput(
                attrs={'class': ' form-control', 'id': 'phoneid', 'placeholder': 'Enter Your Phone'}),
            'age': forms.NumberInput(
                attrs={'class': 'form-control', 'id': 'ageid', 'placeholder': 'Enter Your Age'})
        }


class UserSigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'name': "username", 'id': 'usernameid',
                       'placeholder': 'Enter Your Username'}),
            'password': forms.TextInput(
                attrs={'class': 'form-control',
                       'type': 'password', 'name': "password", 'id': 'passwordid',
                       'placeholder': 'Enter Your Password'})
        }
