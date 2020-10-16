from django.shortcuts import render, redirect
from cashPayment.models import cashPayment

def cashDashboard(request):
    queryset = cashPayment.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, "CashDashboard.html", context)
    

def delete_cash(request, id):
    cashPayment.objects.filter(id=id).delete()

    items = cashPayment.objects.all()

    context = {
        'items': items
    }
    return render(request, "DeletePayment.html", context)
