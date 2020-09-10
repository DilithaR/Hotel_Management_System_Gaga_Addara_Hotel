from django import forms
from .models import Customer


class custmoneForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['cusnic', 'address_l1', 'address_l2', 'postcode']
