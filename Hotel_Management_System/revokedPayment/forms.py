from django.forms import ModelForm
from .models import revokedPayments

class RevForm(ModelForm):
    class Meta:
        model = revokedPayments
        fields = ['Payment_type', 'Paid_amount', 'Rev_amount']