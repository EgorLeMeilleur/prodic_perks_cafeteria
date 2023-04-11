from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'login'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'password'}))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(forms.Form):
    surname = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'aboba'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'aboba'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'aboba'}))
    position = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'aboba'}))
    experience = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'aboba'}))
    city = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'aboba'}))
    balance = forms.DecimalField(label="", widget=forms.TextInput(attrs={'id': 'aboba'}))
    email = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'aboba'}))

