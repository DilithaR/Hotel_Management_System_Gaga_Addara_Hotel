from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from django.contrib.auth.models import auth
import pyodbc

# Create your views here.

def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def vertifyLogin(request):
    custId = 'CUS00001'
    custNIC = '652123215V'
    Email = request.POST['loginEmail']
    Password = request.POST['loginPw']
    customer = Customer(cusid=custId, cusnic=custNIC,
                        email=Email, password=Password)
    customer.save()
    print("Saved Customer")
    return render(request, 'index.html')


# def signUp(request):
#     custId = 'CUS00001'
#     custNIC = '652123215V'
#     Email = request.POST['signEmail']
#     Password = request.POST['signPW']

#     customer = Customer(cusid = custId , cusnic = custNIC , email =Email , password = Password )
#     customer.save()
#     print("Saved Customer")
#     return render(request, 'index.html')



