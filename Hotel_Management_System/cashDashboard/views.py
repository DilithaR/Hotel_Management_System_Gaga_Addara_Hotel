from django.shortcuts import render, redirect
from cashPayment.models import cashPayment
from .filters import CashFilter

def cashDashboard(request):
    queryset = cashPayment.objects.all()

    myFilter = CashFilter(request.GET, queryset = queryset)
    queryset = myFilter.qs

    context = {
        "object_list":queryset, 'myFilter': myFilter
    }
    return render(request, "CashDashboard.html", context)
    

def delete_cash(request, id):
    cashPayment.objects.filter(id=id).delete()

    items = cashPayment.objects.all()

    context = {
        'items': items
    }
    return render(request, "DeletePayment.html", context)
