from django import forms

from django.core.validators import RegexValidator

class BinNumberForm(forms.Form):
    bin_number = forms.IntegerField(widget=forms.NumberInput(), validators=[RegexValidator('^[0-1]+$', message="apenas 0 ou 1")])
