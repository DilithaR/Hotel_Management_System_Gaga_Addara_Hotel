from django.shortcuts import render

def removePayment(request):
    return render(request, "DeletePayment.html")