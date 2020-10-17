from django.shortcuts import render, redirect
from cardPayment.models import cardPayment
from .filters import CardFilter

def cardDashboard(request):
    queryset = cardPayment.objects.all()
    
    myFilter = CardFilter(request.GET, queryset = queryset)
    queryset = myFilter.qs
    
    context = {
        "object_list":queryset, 'myFilter': myFilter
    }
    return render(request, "CardDashboard.html", context)

def delete_card(request, id):
    cardPayment.objects.filter(id=id).delete()

    items = cardPayment.objects.all()

    context = {
        'items': items
    }
    return render(request, "DeletePayment.html", context)
