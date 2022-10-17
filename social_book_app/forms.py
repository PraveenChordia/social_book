from dataclasses import fields
from tabnanny import verbose
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserDetails
from datetime import datetime, date

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDetails
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Invalid Username or Password')


class NewUserCreation(UserCreationForm):
    acc_type = [
        ('Author', 'Author'),
        ('Seller', 'Seller')
    ]
    account_type = forms.ChoiceField(choices=acc_type, widget=forms.RadioSelect)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = UserDetails
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'public_visibility', 'dob', 'age', 'account_type',
            'address', 'about', 'password1', 'password2'
        )


class CustomUserChangeForm(UserChangeForm):
    acc_type = [
        ('Author', 'Author'),
        ('Seller', 'Seller')
    ]
    account_type = forms.ChoiceField(choices=acc_type, widget=forms.RadioSelect)
    class Meta:
        model = UserDetails
        fields = '__all__'