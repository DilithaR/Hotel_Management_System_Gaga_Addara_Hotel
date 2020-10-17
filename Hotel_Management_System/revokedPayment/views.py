from django.shortcuts import render, redirect
from revokedPayment.models import revokedPayments
from .forms import RevForm

def revokedPayment(request):

    form = RevForm()

    if request.method == 'POST':
        form = RevForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/revokedPayment")

    queryset = revokedPayments.objects.all()        

    return render(request, "RevokedPayment.html", {'form':form, "object_list":queryset })