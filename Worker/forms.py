from django import forms
from django.contrib.auth.models import User

from Worker.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'login'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'password'}))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(forms.Form):
    surname = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'surname'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'first_name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'last_name'}))
    position = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'position'}))
    experience = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'experience'}))
    city = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'city'}))
    balance = forms.DecimalField(label="", widget=forms.TextInput(attrs={'id': 'balance'}))
    email = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'email'}))

    class Meta:
        model = Profile
        fields = ('surname', 'first_name', 'last_name', 'email', 'position', 'experience', 'balance', 'city')

