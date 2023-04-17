from django import forms

from Benefits.models import Benefit


class BenefitsForm(forms.ModelForm):
    name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'name'}))
    price = forms.DecimalField(label="", widget=forms.TextInput(attrs={'id': 'price'}))
    city = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'city'}))
    description = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'description'}))

    class Meta:
        model = Benefit
        fields = ('name', 'price', 'city', 'description')
