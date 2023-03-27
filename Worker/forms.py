from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'login'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'password'}))
