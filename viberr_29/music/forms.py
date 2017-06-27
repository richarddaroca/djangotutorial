# this file is for when we are creating new users

from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) # this is used so that our password won't be displayed as a plain text

    class Meta: #this is an information about your class
        model = User                                # User is the table where the users are added
        fields = ['username', 'email', 'password']   # the fields we want the new user to fill in


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

