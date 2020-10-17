import django_filters
from django_filters import CharFilter

from cardPayment.models import cardPayment

class CardFilter(django_filters.FilterSet):

    Month = CharFilter(field_name='Month', lookup_expr='icontains')

    class Meta:
        model = cardPayment
        fields = ['Year', 'Month']