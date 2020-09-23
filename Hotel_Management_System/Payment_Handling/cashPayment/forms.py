from django.forms import ModelForm
from .models import cashPayment

class CashForm(ModelForm):
    class Meta:
        model = cashPayment
        fields = ['Year', 'Month', 'Item_type', 'Item_number', 'Quantity', 'Net_amount']