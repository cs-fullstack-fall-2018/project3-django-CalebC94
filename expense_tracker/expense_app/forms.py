from django import forms
from .models import Account

class Transaction(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
        'name',
        'ammount',
        'date'
]
