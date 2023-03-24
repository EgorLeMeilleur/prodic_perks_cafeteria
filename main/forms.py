from django import forms


class LoginForm(forms.Form):
    usernames = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)