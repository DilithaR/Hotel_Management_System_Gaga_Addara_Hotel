from django.shortcuts import render, redirect  
from hotelpackages.bookingforms import BookingForm  
from hotelpackages.models import Booking 
from hotelpackages.models import Packages,Offers
from hotelpackages.packageform import PackageForm
from hotelpackages.offersform import OffersForm

# Create your views here.  
def booking(request):  
    if request.method == "POST":  
        form = BookingForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/booking')  
            except:  
                pass  
    else:  
        form = BookingForm()  
    return render(request,'booking.html',{'form':form}) 

def viewbooking(request):  
    bookings = Booking.objects.all()  
    return render(request,"viewbooking.html",{'bookings':bookings}) 


def packages(request):  
    if request.method == "POST":  
        form = PackageForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/packages')  
            except:  
                pass  
    else:  
        form = PackageForm()  
    return render(request,'package.html',{'form':form})


def viewpackages(request):  
    packages = Packages.objects.all()  
    return render(request,"viewpackages.html",{'packages':packages})

def modifypackages(request):  
    packages = Packages.objects.all()  
    return render(request,"modifypackages.html",{'packages':packages})

def edit(request, id):  
    packages = Packages.objects.get(id=id)  
    return render(request,'packageedit.html', {'packages':packages})  


def update(request, id):  
    packages = Packages.objects.get(id=id)  
    form = PackageForm(request.POST,request.FILES, instance = packages)  
    if form.is_valid():  
        form.save()  
        return redirect("/modifypackages")  
    return render(request, 'packageedit.html', {'packages': packages})  


def destroy(request, id):  
    packages = Packages.objects.get(id=id)  
    packages.delete()  
    return redirect("/modifypackages") 


def packages_home(request):  
    packages_home = Packages.objects.all() 
    offers= Offers.objects.all()
    return render(request,"packages.html",{'packages_home':packages_home, 'offers':offers})



def offers(request):  
    if request.method == "POST":  
        form = OffersForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/offers')  
            except:  
                pass  
    else:  
        form = OffersForm()  
    return render(request,'offers.html',{'form':form})

def tours(request):  
    tours = Packages.objects.all() 
    return render(request,"tours.html",{'tours':tours})

