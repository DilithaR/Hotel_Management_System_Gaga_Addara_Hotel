import django_filters
from django_filters import CharFilter

from cashPayment.models import cashPayment

class CashFilter(django_filters.FilterSet):

    Month = CharFilter(field_name='Month', lookup_expr='icontains')

    class Meta:
        model = cashPayment
        fields = ['Year', 'Month']