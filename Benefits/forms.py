from django import forms

from Benefits.models import Benefit


class BenefitsForm(forms.ModelForm):
    class Meta:
        model = Benefit
        fields = ('name', 'price', 'city', 'description')
