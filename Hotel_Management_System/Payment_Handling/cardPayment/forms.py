from django.forms import ModelForm
from .models import cardPayment

class CardForm(ModelForm):
    class Meta:
        model = cardPayment
        fields = ['Year', 'Month', 'Card_number', 'Exp_date', 'CRC', 'Amount']