from django.shortcuts import render

def revokedPayment(request):
    return render(request, "RevokedPayment.html")