"""This is signin and signup modelform """

from django import forms
from myapp.models import User


class UserForm(forms.ModelForm):
    """
        User  signup form and fields
    """

    class Meta:
        """
            metaclass for signup form
        """
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'phone', 'age']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'firstnameid',
                       'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'lastnameid',
                       'placeholder': 'Enter Your Last Name'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'id': 'emailid',
                       'placeholder': 'Enter Your Email'}),
            'password': forms.TextInput(
                attrs={'class': 'form-control',
                       'type': 'password', "name": "password", 'id': 'passwordid',
                       'placeholder': 'Enter Your Password'}),
            'phone': forms.NumberInput(
                attrs={'class': ' form-control', 'id': 'phoneid',
                       'placeholder': 'Enter Your Phone'}),
            'age': forms.NumberInput(
                attrs={'class': 'form-control', 'id': 'ageid',
                       'placeholder': 'Enter Your Age'})
        }


class UserSigninForm(forms.ModelForm):
    """
        User signin form and fields
    """

    class Meta:
        """
            metaclass for user signin form
        """
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'name': "email", 'id': 'emailid',
                       'placeholder': 'Enter Your Username'}),

            'password': forms.TextInput(
                attrs={'class': 'form-control',
                       'type': 'password', 'name': "password", 'id': 'passwordid',
                       'placeholder': 'Enter Your Password'})
        }
