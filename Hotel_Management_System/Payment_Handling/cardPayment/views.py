from django.shortcuts import render, redirect
from .forms import CardForm

def cardPayment(request):
    
    form = CardForm()

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form':form}
    return render(request, "CardPayment.html", context)